from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate,logout,login


@login_required(login_url='login_user')
def Baseview(request):
    return render(request,'Landinpage.html')
@login_required(login_url='login_user')
def Adminloginview(request):
    return render(request, 'Adminbase/adminbase.html')
@login_required(login_url='login_user')
def Sellerloginview(request):
    return render(request, 'Sellerbase/sellerbase.html')
@login_required(login_url='login_user')
def Customerloginview(request):
    return render(request, 'Customerbase/customerbase.html')



def loginpage(request):
    if request.method =="POST":
        username=request.POST.get("uname")
        password=request.POST.get('pass')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminloginview')
            elif user.is_Seller:
                return redirect('sellerloginview')
            elif user.is_Customer:
                return redirect('customerloginview')

        else:
            messages.info(request,'Invalid Credentials')


    return render(request,'login.html')



def Logoutrequest(request):
    logout(request)
    return redirect('login_user')
