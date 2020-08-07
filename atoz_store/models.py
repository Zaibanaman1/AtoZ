from django.db import models
from django.contrib.auth.models import User,auth




# Create your models her
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=128,null=True)
    email = models.CharField(max_length=128,null=True)
    
    def __str__(self):
        return self.name



class Product(models.Model):
    catagory_choice = (
        ("FR","fruit"),
        ("DR","dryfruit"),
        ("VG","vegitable"),
        ("oth","other"),   
         )
    name = models.CharField(max_length=128,null=True,)
    catagory = models.CharField(max_length=30,choices= catagory_choice ,null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True,blank=True)
    prodtype =models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
   

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    mark = models.IntegerField(default=1)
    complete = models.BooleanField(default=True,null=True,blank=False)
    transaction_id = models.CharField(max_length=128,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitem=self.orderitem_set.all()
        total = sum([item.get_total for item in orderitem])
        return total

    @property
    def get_cart_items(self):
        orderitem=self.orderitem_set.all()
        total = sum([self.mark for item in orderitem])
        return total 

  

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.DecimalField(decimal_places=3,max_digits=7 ,default=0,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price*self.quantity
        return total


class shipping(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    Order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=400,null=True)
    city = models.CharField(max_length=400,null=True)
    landmark = models.CharField(max_length=400,null=True)
    phonenumber = models.IntegerField(default=404,null=False)
    zipcode = models.CharField(max_length=400,null=True)

    def __str__(self):
        return self.address

class manager(models.Model):
    Orderm=models.CharField(max_length=1000,null=True)
    namem=models.CharField(max_length=400,null=True)
    phonem=models.CharField(max_length=400,null=True)
    trans_id = models.CharField(max_length=400,null=True)
    productm = models.CharField(max_length=400,null=True)
    quantitym=models.CharField(max_length=400,null=True)
    adressm=models.CharField(max_length=400,null=True)
    date = models.DateTimeField(auto_now_add=True)
    totalm = models.CharField(max_length=400,null=True)
    
class extendeduser(models.Model):
    phone_num=models.CharField(max_length=10,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.phone_num


    
    
 

    
    

