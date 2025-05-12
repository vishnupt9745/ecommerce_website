from django.urls import path

from TailWag_Supply_app import views, sellerviews, customerviews, adminviews

urlpatterns = [
    path('',views.Baseview,name='landingpage'),
    path('adminloginview',views.Adminloginview,name='adminloginpage'),
    path('sellerloginview',views.Sellerloginview,name='sellerloginview'),
    path('customerloginview',views.Customerloginview,name='customerloginview'),
    path('login_user',views.loginpage,name='login_user'),


    path('sellerregister',sellerviews.Seller_register,name='sellerregister'),
    path('add_product',sellerviews.Add_product,name='add_product'),
    path("productview_seller",sellerviews.Product_views,name='productview_seller'),
    path('product_delete/<int:id>/',sellerviews.product_delete,name='product_delete'),


    path('customerregister',customerviews.Customer_register,name='customerregister'),
    path('productview_customer',customerviews.Productview,name='productview_customer'),
    path('cart', customerviews.view_cart, name='cart'),
    path('add_to_cart/<int:id>/', customerviews.add_to_cart, name='add_to_cart'),
    path('quantity_increase/<int:id>/',customerviews.quantity_increase,name='quantity_increase'),
    path('quantity_decrease/<int:id>',customerviews.quantity_decrese,name='quantity_decrease'),
    path('buynow/<int:id>/',customerviews.Buy_now,name='buynow'),





    path('customer_details',adminviews.Customer_details,name='customer_details'),
    path('seller_details',adminviews.Seller_details,name='seller_details'),
    path('customer_delete/<int:id>/',adminviews.Customer_delete,name='customer_delete'),
    path('seller_delete/<int:id>/',adminviews.Seller_delete,name='seller_delete'),
    path('productview_admin',adminviews.Product_view,name='productview_admin'),




]
