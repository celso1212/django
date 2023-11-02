from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('search-product/', views.search_product, name='search_product'),
    path('add-products/', views.add_product, name='add_product'),
    path('out_of_stock/', views.out_of_stock, name='out_of_stock'),
    path('delete-product/<int:id>/', views.delete_product, name='delete-product'),
    path('sell-product/<int:id>/', views.sell_product, name='sell-product'),
    path('product-details/<int:id>/', views.product_details, name='product-details')

]