from django.contrib import admin
from .models import *
# Register your models here.
list=[AddCate,CartItem,Cart,AddAddress,PhoneNo,Product,Order,OrderItem,Query,Subscribe]
admin.site.register(list)
