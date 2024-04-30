from django.contrib import admin
from django.urls import path
from .api import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('getRestaurantsInfo/', views.getRestaurantsInfo, name="api_getRestaurantsInfo"),
    path('getCuisines/',views.getCuisines,name="api_getCuisines")
]
