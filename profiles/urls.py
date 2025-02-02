from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path('wishlist', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add/<int:item_id>',
         views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:item_id>',
         views.remove_from_wishlist, name='remove_from_wishlist'),
]
