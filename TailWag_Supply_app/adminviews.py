from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from TailWag_Supply_app.models import Customer, Seller, Product_s, Feedback

@login_required(login_url='login_user')
def Customer_details(request):
    cust_data=Customer.objects.all()

    return render(request,'Adminbase/customer_details.html',{'customer':cust_data})
@login_required(login_url='login_user')
def Seller_details(request):
    sell_data=Seller.objects.all()

    return render(request,'Adminbase/seller_details.html',{'seller':sell_data})
@login_required(login_url='login_user')
def Customer_delete(request,id):
    cust=Customer.objects.get(id=id)
    cust.delete()

    return redirect('customer_details')
@login_required(login_url='login_user')
def Seller_delete(request,id):
    sell=Seller.objects.get(id=id)
    sell.delete()

    return redirect('seller_details')

@login_required(login_url='login_user')
def Product_view(request):
    category = request.GET.get('category')
    if category:
        prod = Product_s.objects.filter(product_category=category)
    else:
        prod = Product_s.objects.all()

    return render(request, 'Adminbase/productview.html', {'product': prod})

@login_required(login_url='login_user')
def feedback_foradmin(request):
    data=Feedback.objects.all()
    return render(request,'Adminbase/feedback_foradmin.html',{'data':data})
@login_required(login_url='login_user')
def Replay(request,id):
    complaint=Feedback.objects.get(id=id)
    if request.method == 'POST':
        r=request.POST.get('reply')#to get the data from frent end 'name=reply'
        print(r)
        complaint.replay=r# to set replay message to replay attribute
        complaint.save()
        messages.info(request,'message is sent now')
        return redirect('feedback_view')

    return render(request,'Adminbase/replaymessage.html',{'complaint':complaint})
