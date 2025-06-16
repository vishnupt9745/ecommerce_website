from django.urls import path

from TailWag_Supply_app import views, sellerviews, customerviews, adminviews

urlpatterns = [
    path('',views.Baseview,name='landingpage'),
    path('adminloginview',views.Adminloginview,name='adminloginview'),
    path('sellerloginview',views.Sellerloginview,name='sellerloginview'),
    path('customerloginview',views.Customerloginview,name='customerloginview'),
    path('login_user',views.loginpage,name='login_user'),
    path('logout',views. Logoutrequest,name='logout'),


    path('sellerregister',sellerviews.Seller_register,name='sellerregister'),
    path('add_product',sellerviews.Add_product,name='add_product'),
    path("productview_seller",sellerviews.Product_views,name='productview_seller'),
    path('product_delete/<int:id>/',sellerviews.product_delete,name='product_delete'),
    path('customer_orders',sellerviews.customer_orders,name='customer_orders'),
    path('work_status_update/<int:id>/',sellerviews.Workstatus,name='work_status_update'),



    path('customerregister',customerviews.Customer_register,name='customerregister'),
    path('productview_customer',customerviews.Productview,name='productview_customer'),
    path('productview_customerall', customerviews.Productviewall, name='productview_customerall'),
    path('cart', customerviews.view_cart, name='cart'),
    path('addto_cart/<int:id>/', customerviews.add_to_cart, name='addto_cart'),
    path('quantity_increase/<int:id>/',customerviews.quantity_increase,name='quantity_increase'),
    path('quantity_decrease/<int:id>',customerviews.quantity_decrese,name='quantity_decrease'),
    path('buynow/<int:id>/',customerviews.Buy_now,name='buynow'),
    path('cart_buy_now/<int:id>/',customerviews.Cart_buynow,name='cart_buy_now'),
    path('myorder',customerviews.my_order_status,name='myorder'),
    path('feedback',customerviews.feedback,name='feedback'),
    path('replay_feedback',customerviews.feedback_replay,name='replay_feedback'),
    path('product_search',customerviews.Product_search,name='product_search'),




    path('customer_details',adminviews.Customer_details,name='customer_details'),
    path('seller_details',adminviews.Seller_details,name='seller_details'),
    path('customer_delete/<int:id>/',adminviews.Customer_delete,name='customer_delete'),
    path('seller_delete/<int:id>/',adminviews.Seller_delete,name='seller_delete'),
    path('productview_admin',adminviews.Product_view,name='productview_admin'),
    path('feedback_view',adminviews.feedback_foradmin,name='feedback_view'),
    path('replaymessage/<int:id>/',adminviews.Replay,name='replaymessage'),




]
