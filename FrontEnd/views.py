from django.shortcuts import render,redirect,get_object_or_404
from BackEnd.models import *
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# from FrontEnd.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
def first(request):
    if request.user.is_authenticated:
        queryset=AddCate.objects.all()
        user_cart_items = CartItem.objects.filter(user=request.user)
        # Calculate total price for each item
        for item in user_cart_items:
            item.total_price = item.get_total_price()

            # Calculate grand total
        grand_total = sum(item.total_price for item in user_cart_items)
        cart_items_count = user_cart_items.count()
        context = {
            'cart_items': user_cart_items,
            'title': 'Canteen',
            'grand_total':grand_total,
            'cart_items_count': cart_items_count,
            'query':queryset,
        }
        if request.method == "POST":
            data = request.POST
            email = data.get('email')
            
            Subscribe.objects.create(
                email=email
            )
            return redirect('/contact_us/')
    else:
        if request.method == "POST":
            data = request.POST
            email = data.get('email')
            
            Subscribe.objects.create(
                email=email
            )
            return redirect('/contact_us/')
        queryset=AddCate.objects.all()
        context={
            'query':queryset,
            'title':'Canteen',
        }
    return render(request,'Front1/fi.html',context)

def contact_us(request):
    if request.user.is_authenticated:
        user_cart_items = CartItem.objects.filter(user=request.user)
        # Calculate total price for each item
        for item in user_cart_items:
            item.total_price = item.get_total_price()

            # Calculate grand total
        grand_total = sum(item.total_price for item in user_cart_items)
        cart_items_count = user_cart_items.count()
        context = {
            'cart_items': user_cart_items,
            'title': 'Contact Us',
            'grand_total':grand_total,
            'cart_items_count': cart_items_count,
            
        }
        
        if request.method == "POST":
            data = request.POST
            fullname = data.get('fullname')
            email = data.get('email')
            phone = data.get('phone')
            subject = data.get('subject')
            msg = data.get('msg')
            
            Query.objects.create(
                fullname=fullname,
                email=email,
                phone=phone,
                subject=subject,
                msg=msg,
            )
            return redirect('/')
    else: 
        if request.method == "POST":
            data = request.POST
            fullname = data.get('fullname')
            email = data.get('email')
            phone = data.get('phone')
            subject = data.get('subject')
            msg = data.get('msg')
            
            Query.objects.create(
                fullname=fullname,
                email=email,
                phone=phone,
                subject=subject,
                msg=msg,
            )
            return redirect('/')
        context = {
            'title':'Contact Us',
        }
    return render(request,'Front1/contact.html',context)

def about_us(request):
    if request.user.is_authenticated:
        user_cart_items = CartItem.objects.filter(user=request.user)
        # Calculate total price for each item
        for item in user_cart_items:
            item.total_price = item.get_total_price()

            # Calculate grand total
        grand_total = sum(item.total_price for item in user_cart_items)
        cart_items_count = user_cart_items.count()
        context = {
            'cart_items': user_cart_items,
            'title': 'About Us',
            'grand_total':grand_total,
            'cart_items_count': cart_items_count,
            
        }
    else:
        context = {
            'title':'About Us',
        }
    return render(request,'Front1/about.html',context)
def homePage(request):
    queryset=AddCate.objects.all()
    context = {
        'title':'Home',
        'query':queryset
    }
    return render(request,'Front1/index.html',context)
def item(request,catname):
    
    if request.user.is_authenticated:
        queryset=AddCate.objects.get(catname=catname)
        queryset1=Product.objects.filter(cname=queryset)
        user_cart_items = CartItem.objects.filter(user=request.user)
        # Calculate total price for each item
        for item in user_cart_items:
            item.total_price = item.get_total_price()

            # Calculate grand total
        grand_total = sum(item.total_price for item in user_cart_items)
        cart_items_count = user_cart_items.count()
        context = {
            'cart_items': user_cart_items,
            'title': 'View Items',
            'grand_total':grand_total,
            'cart_items_count': cart_items_count,
            'query':queryset,
            'query1':queryset1,
        }
    else:
        queryset=AddCate.objects.get(catname=catname)
        queryset1=Product.objects.filter(cname=queryset)
        
        context = {
            'title':'View Items',
            'query':queryset,
            'query1':queryset1,
        }
    return render(request,'Front1/item.html',context)
def view(request,id):
    
    if request.user.is_authenticated:
        queryset=Product.objects.get(id=id) 
        user_cart_items = CartItem.objects.filter(user=request.user)
        # Calculate total price for each item
        for item in user_cart_items:
            item.total_price = item.get_total_price()

            # Calculate grand total
        grand_total = sum(item.total_price for item in user_cart_items)
        cart_items_count = user_cart_items.count()
        context = {
            'cart_items': user_cart_items,
            'title': 'About Us',
            'grand_total':grand_total,
            'cart_items_count': cart_items_count,
            'query':queryset
        }
    else:
        queryset=Product.objects.get(id=id) 
        context={'title':'View Food','query':queryset}
    return render(request,'Front1/viewFood.html',context)
@login_required(login_url="/front/login/")
def addtocartPage(request):
    context={'title':'View Cart'}
    return render(request,'Front1/cart.html',context)
@login_required(login_url="/front/login/")
def cart_items(request):
    if request.user.is_authenticated:
        user_cart_items = CartItem.objects.filter(user=request.user)
        # Calculate total price for each item
        for item in user_cart_items:
            item.total_price = item.get_total_price()

         # Calculate grand total
        grand_total = sum(item.total_price for item in user_cart_items)
        cart_items_count = user_cart_items.count()
        context = {
            'cart_items': user_cart_items,
            'title': 'Add To Cart',
            'grand_total':grand_total,
            'cart_items_count': cart_items_count,
        }
        return render(request, 'Front1/cart_items.html', context)
    else:
        # Handle the case where the user is not authenticated
        return render(request, 'Front1/cart_items.html', {})
#increase or decresed
def increase_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.increase_quantity()
    return redirect('/cart/')  # Redirect to the cart page or any other page you prefer

def decrease_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.decrease_quantity()
    return redirect('/cart/')  # Redirect to the cart page or any other page you prefer

def delete_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('/cart/')  # Redirect to the cart page or any other page you prefer

def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('/cart/')  # Redirect to the cart page or any other page you prefer

#Add To Cart Page
@login_required(login_url="/front/login/")
def add_to_cart(request, id):
    product = get_object_or_404(Product, pk=id)
    user = request.user
    
    # Check if the item is already in the cart for the user
    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)

    # If the item is already in the cart, increase the quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart/') 

@login_required(login_url="/front/login/")
def add_address(request):
    if request.method == "POST":
            data = request.POST
            user = request.user
            fullname = data.get('fullname')
            email = data.get('email')
            address = data.get('address')
            pincode = data.get('pincode')
            mobile = data.get('mobile')
            anysuggession = data.get('anysuggession')
          
            AddRes.objects.create(
                user=user,
                fullname=fullname,
                email=email,
                address=address,
                pincode=pincode,
                mobile=mobile,
                anysuggession=anysuggession
            )
            
            messages.success(request, 'Add Address successfully!!!')
    context = {
        'title':'Add Address',
    }
    return render(request,'Front1/addAddress.html',context)
           
@login_required(login_url="/front/login/")
def checkout(request):
    if request.user.is_authenticated:
        user_cart_items = CartItem.objects.filter(user=request.user)
        # Calculate total price for each item
        for item in user_cart_items:
            item.total_price = item.get_total_price()

         # Calculate grand total
        grand_total = sum(item.total_price for item in user_cart_items)
        cart_items_count = user_cart_items.count()
        # user_cart_items = CartItem.objects.filter(user=request.user)
        if request.method == "POST":
            data = request.POST
            shipping_address_id = data.get('shipping_address')
            payment_method = data.get('payment_method')

            # Create the order
            order = Order.objects.create(
                user=request.user,
                shipping_address=AddRes.objects.get(id=shipping_address_id),
                payment_method=payment_method,
                total_price=grand_total,
            )

            # Associate order items with the order
            for item in user_cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price * item.quantity,
                )

            # Clear the user's cart after the order is placed
            user_cart_items.delete()

            return redirect('order_success')  # Create a view for order success

        queryset = AddRes.objects.filter(user=request.user)
        context = {
            'title':'Check out',
            'cart_items': user_cart_items,
            'query': queryset,
            'grand_total':grand_total,
            'cart_items_count': cart_items_count,
        }
    return render(request,'Front1/checkout.html',context)

@login_required(login_url="/front/login/")
def order_list(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user).order_by('-id')
        user_cart_items = CartItem.objects.filter(user=request.user)
        # Calculate total price for each item
        for item in user_cart_items:
            item.total_price = item.get_total_price()

            # Calculate grand total
        grand_total = sum(item.total_price for item in user_cart_items)
        cart_items_count = user_cart_items.count()
        context = {
            'cart_items': user_cart_items,
            'title': 'Order List',
            'grand_total':grand_total,
            'cart_items_count': cart_items_count,
            'orders': orders,
        }
    return render(request, 'Front1/orderlist.html', context)
@login_required(login_url="/front/login/")
def view_order_list(request,order_item_id):
    order_item = get_object_or_404(OrderItem, id=order_item_id)
    return render(request, 'Front1/vieworderlist.html', {'order_item': order_item,})
@login_required(login_url="/front/login/")
def cancel_order_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Check if the order can be canceled, and update its status
    if order.status in [Order.PENDING, Order.PROCESSING]:
        order.status = Order.CANCELED
        order.save()
        return redirect('/order_list/')
    # Redirect to the order detail page or another appropriate page
    return render(request, 'orderlist.html', {'order': order})
@login_required(login_url="/front/login/")
def order_success(request):
    return render(request, 'Front1/order_success.html')
@login_required(login_url="/front/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

def loginPage(request):
    context={'title':'Login page'}
    if request.method == "POST":
      username=request.POST.get('username')
      password=request.POST.get('password')

      if not User.objects.filter(username=username).exists():
        messages.error(request,'Invalid Username')
        return redirect('/front/login/')
      
      user=authenticate(username=username,password=password)

      if user is None:
        messages.error(request,'Invalid Password')
        return redirect('/front/login/')
      else:
        login(request,user)
        request.session['user_authenticated'] = True
        return redirect('/')
    return render(request,"Front1/login.html",context)
def regPage(request):
    if request.method =="POST":
       first_name=request.POST.get('first_name')
       username=request.POST.get('username')
       password=request.POST.get('password')
       email=request.POST.get('email')
       
       user=User.objects.filter(username=username)
       if user.exists():
           messages.info(request,'User already taken')
           return redirect('/front/reg/')
       user = User.objects.create(
           first_name=first_name,
           username=username,
           email=email,
       )
       user.set_password(password)
       user.save()
       request.session['user_authenticated'] = True
       messages.info(request,'Account sucessfully created')
       return redirect('/front/login/')
    
    context={'title':'View Team'}
    return render(request,'Front1/reg.html',context)
def logoutPage(request):
   logout(request)
   return redirect('/')
