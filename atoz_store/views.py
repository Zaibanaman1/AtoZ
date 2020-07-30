from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import datetime
import json
from . utils import cookieCart
from django.contrib.auth.models import User,auth
from decimal import Decimal

# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request ,'atoz_store/store.html',context)


def cart(request):
    
    if request.user.is_authenticated:
        email = request.user.email
        name = request.user.first_name
        customer,created = Customer.objects.get_or_create(
            email=email,
        )
        customer.name = name
        customer.save()
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    

    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
            
        except:
            cart = {}
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartitems = order['get_cart_items']
        
        for  i  in cart:
            try:
                cartitems += Decimal(cart[i]['quantity'])
                product = Product.objects.get(id=i)
                Flag = product.prodtype
                total = (product.price * Decimal(cart[i]['quantity']))
                order['get_cart_total'] +=  total
                order['get_cart_items'] +=  cart[i]['quantity']       
                item ={
                        'product':{
                        'id':product.id,
                        'name':product.name,
                        'price':product.price,
                        'imageURL':product.imageURL,
                        'flag':Flag,
                        
                    },
                    'quantity':cart[i]['quantity'],
                    'get_total':total
                    }
                items.append(item)
                
            
            except:
                pass
   
    context = {'items':items,'order':order,'cartitems':cartitems}
    return render(request,'atoz_Store/cart.html',context)

def checkout(request):
     if request.user.is_authenticated:
        email = request.user.email
        name = request.user.first_name
        customer,created = Customer.objects.get_or_create(
            email=email,
        )
        customer.name = name
        customer.save()
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
     else:
        cookieData = cookieCart(request)
        cartitems = cookieData['cartitems']
        order = cookieData['order']
        items = cookieData['items']
   
     context = {'items':items,'order':order,'cartitems':cartitems}
    
     return render(request, 'atoz_store/checkout.html',context)

def user(request):
    user_list = user.objects.order_by('first_name')
    user_dict = {'user':user_list}
    return render(request,'atoz_store/user/add.html',context=user_dict)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('productId:',productId)
    email = request.user.email
    name = request.user.first_name
    customer,created = Customer.objects.get_or_create(
            email=email,
        )
    customer.name = name
    customer.save()
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        if product.prodtype: 
            orderItem.quantity = (orderItem.quantity + Decimal(0.25))
        else:    
            orderItem.quantity = (orderItem.quantity + Decimal(1.00))
    elif action == 'remove':
        if product.prodtype:
            orderItem.quantity = (orderItem.quantity - Decimal(0.25) )
        else:            
            orderItem.quantity = (orderItem.quantity - Decimal(1.00) )
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse(" ",safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().time()
    data = json.loads(request.body)
    print('Data:',request.body)
    if request.user.is_authenticated:
        email = request.user.email
        name = request.user.first_name
        customer,created = Customer.objects.get_or_create(
            email=email,
        )
        customer.name = name
        customer.save()
        order, created = Order.objects.get_or_create(customer=customer,complete= False)
        order.save()
        
   
        print(shipping)
    else:
        print("user is not logged in...")
        print('cookies:',request.COOKIES)
        name = data['form']['name']
        email = data['form']['email']
        cookieData = cookieCart(request)
        items = cookieData['items']
        customer,created = Customer.objects.get_or_create(
            email=email,
        )
        customer.name = name
        customer.save()
        order = Order.objects.create(
            customer=customer,
            complete=False
        )
        for item in items:
            product = Product.objects.get(id=item['product']['id'])
            orderItem = OrderItem.objects.create(
                product=product,
                order=order,
                quantity=item['quantity']
            )
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
            order.complete=True
    order.save()
    usernow=request.user
    ext = extendeduser.objects.get(user=usernow)
    if request.user.is_authenticated:
        shipping.objects.create(
        customer=customer,
        Order=order,
        address=data['shipping']['address'],
        city = data['shipping']['city'],
        landmark = data['shipping']['landmark'],
        phonenumber = ext.phone_num,
        zipcode = data['shipping']['zipcode'],
         )
    else:
        shipping.objects.create(
        customer=customer,
        Order=order,
        address=data['shipping']['address'],
        city = data['shipping']['city'],
        landmark = data['shipping']['landmark'],
        phonenumber = data['shipping']['phonenumber'],
        zipcode = data['shipping']['zipcode'],
         )     
    name = data['form']['name']
    address=data['shipping']['address'],
    city = data['shipping']['city'],
    landmark = data['shipping']['landmark'],
    
    if request.user.is_authenticated:
        phonenumber=ext.phone_num
        print(phonenumber)
    else:
        phonenumber = data['shipping']['phonenumber'],
    zipcode = data['shipping']['zipcode']
    items = order.orderitem_set.all()
    productmname = []
    
    for item in items:
        pack =str(item.product.name) + ":" + str(item.product.price) +"x"+str(item.quantity)
        flag = item.product.prodtype
        if flag:
            pack = pack + 'kg'
        else:
            pack = pack + "peice"
        productmname.append(pack)
        print(productmname)         
    disadress = str(address)  + "\n" + "landmark:"+ str(landmark) + str(city) + "\n" +  str(zipcode)

    

    manager.objects.create(
        Orderm = order,
        namem = customer.name,
        phonem = phonenumber,
        trans_id = transaction_id,
        productm =str(productmname),
        totalm = str(total),
        adressm = disadress
    )

                
    return JsonResponse("payment submitted", safe = False)

#def search(request):
    
def profile(request):
    return render(request,'atoz_store/profile.html')    