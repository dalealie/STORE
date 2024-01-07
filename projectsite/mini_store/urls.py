from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.all_categories, name='all_categories'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('customer/<int:customer_id>/create_order/', views.create_order, name='create_order'),
    # Add other URL patterns as needed for your application
]
