from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cloudinary.uploader import upload
# Create your views here.
def loginPage(request):
    context={'title':'Admin Login'}
    if request.method == "POST":
      username=request.POST.get('username')
      password=request.POST.get('password')

      if not User.objects.filter(username=username).exists():
        messages.error(request,'Invalid Username')
        return redirect('/')
      
      user=authenticate(username=username,password=password)

      if user is None:
        messages.error(request,'Invalid Password')
        return redirect('/')
      else:
        login(request,user)
        messages.error(request,'Login User')
        return redirect('/back/menu/')
    return render(request,'login.html',context)
@login_required(login_url='/back/')
def regPage(request):
    context={'title':'Registration Page'}
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'User already taken')
            return redirect('/back/reg/')
        user = User.objects.create(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account sucessfully created')
        return redirect('/back/reg/')
    return render(request,'registration.html',context)
@login_required(login_url='/back/')
def logoutPage(request):
   logout(request)
   return redirect('/back/')
@login_required(login_url='/back/')
def menu(request):
    queryset=AddCate.objects.all()
    context={'title':'view menu','query':queryset}
    return render(request,'menu.html',context)
@login_required(login_url='/back/')
def item(request):
    queryset=Product.objects.all()
    context={'title':'View Items','q1':queryset}
    return render(request,'item.html',context)
@login_required(login_url='/log/')
def item1(request,catname):
    queryset=AddCate.objects.get(catname=catname)
    queryset2=Product.objects.filter(cname=queryset)
    context={'title':'View Items','query1':queryset,'q1':queryset2}
    return render(request,'item.html',context)
@login_required(login_url='/back/')
def addItem(request):
    choice1=AddCate.objects.all()
    choice=['Select Option','SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THRUSDAY','FRIDAY','SATURDAY',]
    context={'title':'Add Items','dyn':choice,'dyn1':choice1}
    if request.method=="POST":
        data=request.POST
        cname=data.get('cname')
        week=data.get('week')
        img=request.FILES.get('img')
        fname=data.get('fname')
        desc=data.get('desc')
        price=data.get('price')
        quantity=data.get('quantity')
        cname_instance = AddCate.objects.get(catname=cname)
        Product.objects.create(cname=cname_instance,week=week,img=img,fname=fname,desc=desc,price=price,quantity=quantity)
        messages.success(request,'Add record Sucessfully!!!')
        # return redirect('/')
    
    return render(request,'addItem.html',context)
@login_required(login_url='/back/')
def updateItem(request,id):
    queryset=Product.objects.get(id=id)
    choice1=AddCate.objects.all()
    choice=['Select Option','SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THRUSDAY','FRIDAY','SATURDAY',]
    print(choice)
    context={'title':'Update Items','dyn':choice,'dyn1':choice1,'q1':queryset}
    if request.method=="POST":
        data=request.POST
        cname=data.get('cname')
        week=data.get('week')
        img=request.FILES.get('img')
        fname=data.get('fname')
        desc=data.get('desc')
        price=data.get('price')
        quantity=data.get('quantity')
        cname_instance = AddCate.objects.get(catname=cname)
        queryset.cname=cname_instance
        queryset.week=week
        queryset.fname=fname
        queryset.desc=desc
        queryset.price=price
        queryset.quantity=quantity
        if img:
            queryset.img=img
        queryset.save() 
        messages.success(request,'Update record Sucessfully!!!')
        return redirect('/back/menu/')
    return render(request,'addItem.html',context)
@login_required(login_url='/back/')
def deleteItem(request,id):
    context={'title':'Delete'}
    queryset=Product.objects.get(id=id)
    queryset.delete()
    messages.success(request,'Delete Sucessfully!!!')
    return redirect('/back/menu/',context)
@login_required(login_url='/back/')
def addcate(request):
    context={'title':'Add Categories'}
    if request.method=="POST":
        data=request.POST
        img=request.FILES.get('img')
        # Upload the file to Cloudinary
        result = upload(img)
        catname=data.get('catname')
        AddCate.objects.create(img=result,catname=catname)
        
        messages.success(request,'Add record Sucessfully!!!')
        return redirect('/back/menu/')
    
    return render(request,'addcategories.html',context)
@login_required(login_url='/back/')
def editCate(request,id):
    queryset=AddCate.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        img=request.FILES.get('img')
        catname=data.get('catname')
        queryset.catname=catname
        if img:
            queryset.img=img
        queryset.save()    
        messages.success(request,'Update record Sucessfully!!!')
        return redirect('/back/menu/')
    context={'title':'Update categories','update':queryset}
    return render(request,'addcategories.html',context)
@login_required(login_url='/back/')
def deleteCate(request,id):
    context={'title':'Delete'}
    queryset=AddCate.objects.get(id=id)
    queryset.delete()
    messages.success(request,'Delete Sucessfully!!!')
    return redirect('/back/menu/',context)
@login_required(login_url='/back/')
def stock(request):
    return render(request,'stock.html')
@login_required(login_url='/back/')
def payment(request):
    return render(request,'payment.html')
def live(request):
    return render(request,'live.html')