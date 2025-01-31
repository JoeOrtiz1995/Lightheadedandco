from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.about_us, name='about'),
  path('<int:testimonial_id>/', views.about_us, name='about'),
  path('edit/<int:testimonial_id>/', views.edit_testimonial, name='edit_testimonial'),
  path('delete/<int:testimonial_id>/', views.delete_testimonial, name='delete_testimonial'),
]