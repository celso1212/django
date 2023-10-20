from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('product-details/<int:id>/', views.product_details, name='product-details')
]