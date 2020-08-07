from django.shortcuts import render,redirect
from django.contrib import messages
from atoz_store.models import * 
from django.contrib.auth.models import User,auth

# Create your views here.

def register(request):



    if request.method== 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        usernamee= request.POST['username']
        username=usernamee.lower()
        phone_no = request.POST['phone']
        password1= request.POST['password1']
        password2= request.POST['password2']
        email= request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            if username=="" or password1=="":
                messages.info(request,"please fill all the fields ")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
           
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                extended = extendeduser(phone_num=phone_no,user=user)
                extended.save()
                print('user created')

                return redirect("login")

        else:

            messages.info(request,"password did not match")
            return redirect('register')
   
        return redirect("/")
    else:

        return render(request,'atoz_store/register.html')

def login(request):
    if request.method == 'POST':
          username= request.POST['login_username']
          password= request.POST['login_password']

          user=auth.authenticate(username=username,password=password)
          if user is not None:
              auth.login(request,user)
              return redirect("/")
          else:
              messages.info(request,"invalid credentials")
              return redirect('login')

    else:
        return render(request,'atoz_store/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')       
def forgotpassword(request):
    return render(request,'atoz_store/forgotpassword.html')
    

