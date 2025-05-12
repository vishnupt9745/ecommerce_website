from django.shortcuts import render, redirect

from TailWag_Supply_app.forms import LoginRegister, SellerForm, ProductForm
from TailWag_Supply_app.models import Seller, Product_s


def Seller_register(request):
    login_form=LoginRegister()
    seller_form=SellerForm()

    if request.method =="POST":
        logindata=LoginRegister(request.POST)
        sellerform=SellerForm(request.POST)

        if logindata.is_valid() and sellerform.is_valid():
            seller=logindata.save(commit=False)
            seller.is_Seller=True
            seller.save()


            user1=sellerform.save(commit=False)
            user1.user=seller
            user1.save()


            return redirect('login_user')

    return render(request,'sellerregistration.html',{'login_data':login_form,'seller_data':seller_form})


def Add_product(request):
    seller = request.user.seller
    seller1=request.user
    print(seller1.id)
    print(seller.id)

    product_form=ProductForm()
    if request.method == "POST":
        prod=ProductForm(request.POST,request.FILES)
        if prod.is_valid():
            product=prod.save(commit=False)
            product.product_user=seller
            product.save()
    return render(request,'Sellerbase/add_product.html',{'product_form':product_form})


def Product_views(request):
    current_user=request.user
    user_id=Seller.objects.get(user=current_user)
    data=Product_s.objects.filter(product_user=user_id)
    print(data)

    return render(request,'Sellerbase/seller_productview.html',{'datas':data})


def product_delete(request, id):
    prod = Product_s.objects.get(id=id)
    prod.delete()

    return redirect("productview_seller")



