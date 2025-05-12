from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate,logout,login



# Create your views here.
def Baseview(request):
    return render(request,'Landinpage.html')

def Adminloginview(request):
    return render(request, 'Adminbase/adminbase.html')

def Sellerloginview(request):
    return render(request, 'Sellerbase/sellerbase.html')

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




