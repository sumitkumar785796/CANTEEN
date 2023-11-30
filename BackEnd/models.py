from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AddCate(models.Model):
    # img=CloudinaryField('img')
    img=models.URLField()
    catname=models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.catname
      
class Product(models.Model):
    SUNDAY = 'SUNDAY'
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THRUSDAY = 'THRUSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'

    WEEK_CHOICES = [
        (SUNDAY ,'SUNDAY'),
        (MONDAY , 'MONDAY'),
        (TUESDAY , 'TUESDAY'),
        (WEDNESDAY , 'WEDNESDAY'),
        (THRUSDAY , 'THRUSDAY'),
        (FRIDAY, 'FRIDAY'),
        (SATURDAY, 'SATURDAY'),
    ]
    cname=models.ForeignKey(AddCate,related_name='categories',on_delete=models.CASCADE)
    week=models.CharField(max_length=100 , choices=WEEK_CHOICES, default=SUNDAY)
  
    # img=CloudinaryField('img')
    img=models.URLField()
    fname=models.CharField(max_length=500)
    desc=models.TextField()
    price=models.IntegerField(null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    def __str__(self) -> str:
        return self.fname 

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.quantity} x {self.product.fname} in cart"
    
    def increase_quantity(self):
        self.quantity += 1
        self.save()

    def decrease_quantity(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.save()
        else:
            self.delete()
    
    def get_total_price(self):
        return self.quantity * self.product.price

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    def __str__(self):
        return f"Cart for {self.user.username}"

class AddAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    fullname=models.CharField(max_length=300,null=True)
    email=models.EmailField(null=True,unique=True)
    address=models.TextField(null=True)
    pincode=models.IntegerField(null=True)
    mobile=models.CharField(max_length=15)
    anysuggession=models.TextField(null=True)
    def __str__(self) -> str:
        return self.fullname
    
class Order(models.Model):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'
    CANCELED = 'Canceled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
        (CANCELED, 'Canceled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(AddAddress, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255)  # You may want to use choices for payment methods
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
    def cancel_order_by_user(self):
        if self.status == self.PENDING or self.status == self.PROCESSING:
            self.status = self.CANCELED
            self.save()

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.fname} - {self.order}"
    
class Query(models.Model):
    fullname=models.CharField(max_length=200,null=True)
    email=models.EmailField()
    phone=models.IntegerField()
    subject=models.TextField()
    msg=models.TextField()
    def __str__(self) -> str:
        return self.fullname
class Subscribe(models.Model):
    email=models.EmailField()
    def __str__(self) -> str:
        return self.email