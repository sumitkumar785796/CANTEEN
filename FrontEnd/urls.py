from django.urls import path,include
from .views import *
urlpatterns = [
    path('',first,name='first'),
    path('contact_us/',contact_us,name='contact_us'),
    path('about_us/',about_us,name='about_us'),
    path('front1/item/<catname>/', item,name='item'),
    path('front1/view/<id>/', view,name='view'),
    path('cart/', cart_items, name='cart_items'),
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('increase_quantity/<int:cart_item_id>/', increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:cart_item_id>/', decrease_quantity, name='decrease_quantity'),
    path('delete_cart_item/<int:cart_item_id>/', delete_cart_item, name='delete_cart_item'),
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('add_address/', add_address, name='add_address'),
    path('order_success/', order_success, name='order_success'),
    path('order_list/', order_list, name='order_list'),
    path('view_order_list/<int:order_item_id>', view_order_list, name='view_order_list'),
    path('cancel_order/<int:order_id>/', cancel_order_view, name='cancel_order'),

    path('', homePage,name='homePage'),
    path('front1/Cart/', addtocartPage,name='addtocartPage'),
    path('front1/checkout/', checkout,name='checkout'),
    path('front/login/', loginPage,name='loginPage'),
    path('front/reg/', regPage,name='regPage'),
    path('front/logout/', logoutPage,name='logoutPage'),
]