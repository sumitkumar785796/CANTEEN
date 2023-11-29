from django.urls import path,include
from .views import *
urlpatterns = [
    path('superuser/', superuser_registration, name='superuser_registration'),
    path('back/',loginPage,name='loginPage'),
    path('back/reg/',regPage,name='regPage'),
    path('back/log/',logoutPage,name='logoutPage'),
    path('back/menu/',menu,name='menu'),
    path('back/addcate/',addcate,name='addcate'),
    path('back/Editcate/<id>/',editCate,name='editCate'),
    path('back/Delcate/<id>/',deleteCate,name='deleteCate'),
    path('back/item/',item,name='item'),
    path('back/item/<catname>/',item1,name='item1'),
    path('back/addItem/',addItem,name='addItem'),
    path('back/editItem/<id>/',updateItem,name='updateItem'),
    path('back/deleteItem/<id>/',deleteItem,name='deleteItem'),
    path('back/stock/',stock,name='stock'),
    path('back/payment/',payment,name='payment'),
]
