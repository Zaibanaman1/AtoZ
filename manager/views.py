from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from atoz_store.models import *
from django.http import JsonResponse
import json
import ast
# Create your views here.
def loginm(request):
    if request.method == 'POST':
          username= request.POST['login_username']
          password= request.POST['login_password']

          user=auth.authenticate(username=username,password=password)
          if user is not None and user.is_superuser:
                auth.login(request,user)
                return redirect("managerdash")
          else:
              messages.info(request,"invalid credentials")
              return redirect('/')

    else:
        return render(request,'atoz_store/managelogin.html')

def logout(request):
    
    auth.logout(request)
    return redirect('/')

     
  


def managerdash(request):
    user = request.user
    if user is not None and user.is_superuser:
        managerda = list(manager.objects.all())
        orderss= Order.objects.all()
        orders = list(Order.objects.all())
        customers = list(Customer.objects.all())
        if request.method == "POST":
            status = request.POST['status']
            print(status)
            dictt = json.loads(status) 
            print(dictt)
            
            ordernum =   int(dictt['ordno'])

            print(ordernum)
            num = ordernum 
            print(num)
            st = dictt['status']
          
            print(dictt['status'])
  
            ord  = Order.objects.get(id=num)
            ord.status = st
            ord.save()
        
          
           
            
           
         
            
     
        context = {'customers':customers,'orders':orders,'managerda':managerda}
        return render(request,'atoz_store/manager.html',context)
    else:
        return render(request,'atoz_store/managelogin.html')
     
           