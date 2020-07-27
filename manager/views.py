from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from atoz_store.models import *
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
        print(managerda)
        orders = list(Order.objects.all())
        customers = list(Customer.objects.all()) 
        context = {'customers':customers,'orders':orders,'managerda':managerda}
        return render(request,'atoz_store/manager.html',context)
    else:
        return render(request,'atoz_store/managelogin.html')
    
           