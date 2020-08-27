import json
from . models import *
from decimal import Decimal

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
        print(cart)
            
    except:
        cart = {}
    items = []
    order = {'get_cart_total':0,'get_cart_items':0}
    cartitems = order['get_cart_items']
        
    for  i  in cart:
        try:
            cartitems += 1
            print(cartitems)
            product = Product.objects.get(id=i)
            total = (product.price * Decimal(cart[i]['quantity']))
            order['get_cart_total'] +=  total
            order['get_cart_items'] +=  cartitems
            item ={
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'imageURL':product.imageURL,
                },
                'quantity': cart[i]['quantity'],
                'get_total':total
                }
            items.append(item)
        except:
            pass    
    return{'order':order,'items':items,'cartitems':cartitems}

    

def billingsum(request):

    items = []
    order = {'get_cart_total':0,'get_cart_items':0}
    cartitems = order['get_cart_items']
        
    for  i  in cart:
            try:
                cartitems += cart[i]['quantity']
                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quantity'])
                order['get_cart_total'] +=  total
                order['get_cart_items'] +=  cart[i]['quantity']
                item ={
                    'product':{
                        'id':product.id,
                        'name':product.name,
                        'price':product.price,
                        
                    },
                    'quantity':cart[i]['quantity'],
                    'get_total':total
                }
                items.append(item)
            except:
                pass
    print(items)   


