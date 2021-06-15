from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name="AboutUS"),
    path('contact/', views.contact, name="contactUS"),
    path('tracker/', views.tracker, name="Trackingstatus"),
    path('search/', views.search, name="search"),
    path('products/<int:myid>', views.productView, name="Productview"),
    path('checkout/', views.checkout, name="checkout"),
]