#url/products.py
from django.urls import path
from . import views  # Import views from products app
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('products/', views.product_list, name='product_list'),  # Display product list
    path('products/add/', views.add_product, name='add_product'),  # Add new product
    path('products/edit/<int:id>/', views.edit_product, name='edit_product'),  # Edit product
    path('products/delete/<int:id>/', views.delete_product, name='delete_product'),  # Delete product
    path('orders/', views.order_list, name='order_list'),  # Order list
    path('orders/create/', views.create_order, name='create_order'),  # Create new order
    path('sales_report/', views.sales_report, name='sales_report'),  # Sales report
    path('', views.home, name='home'), 
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # ตั้งค่า redirect หลัง logout
    
]
