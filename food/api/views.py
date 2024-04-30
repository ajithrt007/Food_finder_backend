from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Restaurants, CuisinesRest, Cuisines
from .serializers import FilterSortSerializer, RestaurantSerializer, CuisineSerializer
from django.db.models import Q

@api_view(['GET'])
def getRestaurantsInfo(request):
    filter_sort_serializer=FilterSortSerializer(data=request.query_params)
    filter_sort_serializer.is_valid(raise_exception=True)

    rating_low=filter_sort_serializer.validated_data.get('rating_low')
    rating_high=filter_sort_serializer.validated_data.get('rating_high')
    if rating_low is not None and rating_high is not None:
        query=Q(rating__gte=rating_low,rating__lte=rating_high)

    has_table_booking=filter_sort_serializer.validated_data.get('has_table_booking')
    if has_table_booking == 1:
        query&=Q(has_table=True)
    else:
        query&=Q(has_table=False)

    has_online_delivery=filter_sort_serializer.validated_data.get('has_online_delivery')
    if has_online_delivery == 1:
        query&=Q(has_delivery=True)
    else:
        query&=Q(has_delivery=False)

    cuisine_list=filter_sort_serializer.validated_data.get('cuisine')
    if cuisine_list != []:
        matched_cuisines_ids=Cuisines.objects.filter(cuisine__in=cuisine_list).values_list('id',flat=True)
        matched_restaurants_ids=CuisinesRest.objects.filter(cuisine__in=matched_cuisines_ids).values_list('restaurant',flat=True)
        query&=Q(rest_id__in=matched_restaurants_ids)

    search_string=filter_sort_serializer.validated_data.get('search_string')
    if search_string:
        query&=Q(name__istartswith=search_string)

    try:
        filtered_queryset=Restaurants.objects.filter(query)
    except Exception as  e:
        return Response({'error': str(e)})
    
    sorting_fielding=filter_sort_serializer.validated_data.get('sort_by')
    sorting_order=filter_sort_serializer.validated_data.get('order')
    sorting_prefix= '-' if sorting_order=='descending' else ''
    sorted_queryset=filtered_queryset.order_by(f"{sorting_prefix}{sorting_fielding}")    

    page_size=filter_sort_serializer.validated_data.get('page_size')
    page_no=filter_sort_serializer.validated_data.get('page_no')
    
    start_index = page_no * page_size
    end_index = start_index + page_size

    try:
        if end_index>filtered_queryset.count():
            paginated_queryset=sorted_queryset[start_index:]
        else:
            paginated_queryset=sorted_queryset[start_index:end_index]
    except IndexError:
        print("List Index out of range")

    response=RestaurantSerializer(paginated_queryset,many=True)

    return Response({"response": response.data, "count": paginated_queryset.count(), "total": filtered_queryset.count()})


@api_view(['GET'])
def getCuisines(request):
    response=Cuisines.objects.all()
    cuisine_serilaizer=CuisineSerializer(response,many=True)
    return Response({"cuisines": cuisine_serilaizer.data, "count": response.count()})