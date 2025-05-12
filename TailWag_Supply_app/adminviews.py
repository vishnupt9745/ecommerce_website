from django.shortcuts import render, redirect

from TailWag_Supply_app.models import Customer, Seller, Product_s


def Customer_details(request):
    cust_data=Customer.objects.all()

    return render(request,'Adminbase/customer_details.html',{'customer':cust_data})

def Seller_details(request):
    sell_data=Seller.objects.all()

    return render(request,'Adminbase/seller_details.html',{'seller':sell_data})

def Customer_delete(request,id):
    cust=Customer.objects.get(id=id)
    cust.delete()

    return redirect('customer_details')

def Seller_delete(request,id):
    sell=Seller.objects.get(id=id)
    sell.delete()

    return redirect('seller_details')


def Product_view(request):
    category = request.GET.get('category')
    if category:
        prod = Product_s.objects.filter(product_category=category)
    else:
        prod = Product_s.objects.all()

    return render(request, 'Adminbase/productview.html', {'product': prod})
