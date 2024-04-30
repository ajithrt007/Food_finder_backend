from rest_framework import serializers
from ..models import Restaurants,Cuisines

INT_CHOICES=(1,0,-1)
SORT_CHOICES=('ascending','descending')
SORTING_CHOICES=('name','rating','avg_cost','price_range','votes')

class FilterSortSerializer(serializers.Serializer):
    sort_by=serializers.ChoiceField(required=False,default='rating',choices=SORTING_CHOICES)
    order=serializers.ChoiceField(required=False,choices=SORT_CHOICES,default='descending')
    
    rating_low=serializers.FloatField(required=False,default=0)
    rating_high=serializers.FloatField(required=False,default=5)
    has_table_booking=serializers.ChoiceField(required=False,default=0,choices=INT_CHOICES)
    has_online_delivery=serializers.ChoiceField(required=False,default=0,choices=INT_CHOICES)
    cuisine=serializers.ListField(
        child=serializers.CharField(required=False),
        required=False,
        default=[],
        allow_empty=True
    )
    search_string=serializers.CharField(required=False)
    page_size=serializers.IntegerField(required=False, default=20, max_value=50)
    page_no=serializers.IntegerField(required=False,default=0)


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = '__all__'

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cuisines
        fields = '__all__'