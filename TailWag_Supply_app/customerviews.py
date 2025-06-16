from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from TailWag_Supply_app.forms import LoginRegister, CustomerForm, BuynowForm, ReplayForm
from TailWag_Supply_app.models import Product_s, Customer, CartItem, Buynow_data, Feedback


def Customer_register(request):
    login_form=LoginRegister()
    customer_form=CustomerForm()
    if request.method == "POST":
        logindata=LoginRegister(request.POST)
        customerdata=CustomerForm(request.POST)

        if logindata.is_valid() and customerdata.is_valid():
            customer=logindata.save(commit=False)
            customer.is_Customer=True
            customer.save()
            print(customer)

            user1=customerdata.save(commit=False)
            user1.user=customer
            user1.save()
            print(user1)

            return redirect('login_user')



    return render(request,'customerregistration.html',{'login_data':login_form,'customer_data':customer_form})

@login_required(login_url='login_user')
#customer view on product
def Productviewall(request):
    prod = Product_s.objects.all()
    return render(request, 'Customerbase/productview.html', {'product': prod})
@login_required(login_url='login_user')
def Productview(request):
    category = request.GET.get('category')
    prod = Product_s.objects.filter(product_category=category)

    return render(request, 'Customerbase/productview.html', {'product': prod})
@login_required(login_url='login_user')
def add_to_cart(request, id):
    # Try to get the selected product
    customer=Customer.objects.get(user=request.user)
    product = Product_s.objects.get(id=id)


    # Try to find the cart item for this product and user
    try:
        cart_item = CartItem.objects.get(product=product, user=customer)
        cart_item.quantity += 1  # Increase quantity if already in cart

    except CartItem.DoesNotExist:
        cart_item = CartItem(product=product, user=customer, quantity=1)  # Create new cart item

    cart_item.save()

    return redirect('cart')
@login_required(login_url='login_user')
def view_cart(request):
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return redirect('productview_customer')  # If customer doesn't exist, redirect to customer view

    # Fetch all cart items for this customer
    cart_items = CartItem.objects.filter(user=customer, is_purchased=False)


    # Calculate total price for each item in the cart
    for item in cart_items:
        item.total_item_price = item.product.product_price * item.quantity

    # Calculate the overall total price for the cart
    total_price = sum(item.total_item_price for item in cart_items)

    # Pass the cart items and total price to the template
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'Customerbase/cart_view.html', context)


@login_required(login_url='login_user')
def quantity_increase(request,id):

    increase=CartItem.objects.get(id=id)
    increase.quantity =increase.quantity +1
    increase.save()

    return redirect('cart')

@login_required(login_url='login_user')
def quantity_decrese(request,id):
    try:
        decrese=CartItem.objects.get(id=id)
        decrese.quantity=decrese.quantity-1

        if decrese.quantity ==0:
            decrese.delete()

        else:
            decrese.save()
    except CartItem.DoesNotExist:
        pass

    return redirect('cart')

@login_required(login_url='login_user')
def Buy_now(request, id):
    product = get_object_or_404(Product_s, id=id)
    customer = Customer.objects.get(user=request.user)
    seller = product.product_user

    if request.method == "POST":
        form = BuynowForm(request.POST)
        if form.is_valid():
            buy_now = form.save(commit=False)
            buy_now.customer = customer
            buy_now.seller = seller
            buy_now.product = product
            buy_now.order_date = datetime.now()
            buy_now.is_paid = True


            quantity_requested = form.cleaned_data['quantity']

            product.product_count -= quantity_requested

            product.save()




            buy_now.save()
            return render(request,'Customerbase/paymentsuccessfull.html')
    else:
        form = BuynowForm()

    return render(request, 'Customerbase/buy_now.html', {
        'buynow': form,
        'buy_data': product
    })



@login_required(login_url='login_user')
def Cart_buynow(request, id):
    product = get_object_or_404(Product_s, id=id)

    customer = get_object_or_404(Customer, user=request.user)
    seller = product.product_user

    if request.method == "POST":
        form = BuynowForm(request.POST)
        if form.is_valid():
            quantity_requested = int(request.POST.get('quantity', 1))

            if product.product_count < quantity_requested:
                messages.warning(request, "Requested quantity exceeds available stock.")
                return redirect('buynow', id=product.id)

            buy_now = form.save(commit=False)
            buy_now.customer = customer
            buy_now.seller = seller
            buy_now.product = product
            buy_now.order_date = datetime.now()
            buy_now.is_paid = True

            product.product_count -= quantity_requested
            product.save()
            buy_now.save()

            cart_item = CartItem.objects.filter(user=customer, product=product).first()
            if cart_item:
                cart_item.is_purchased = True
                cart_item.save()

            return redirect('payment_success_url')  # Or render if needed
    else:
        form = BuynowForm()

    return render(request, 'Customerbase/buy_now.html', {
        'buynow': form,
        'buy_data': product
    })

@login_required(login_url='login_user')
def my_order_status(request):
    user=request.user
    customer = Customer.objects.get(user=user)
    orders = Buynow_data.objects.filter(customer=customer)

    return render(request,'Customerbase/my_order.html',{'order':orders})
@login_required(login_url='login_user')
def feedback(request):
    form = ReplayForm()
    if request.method == "POST":
        user = request.user
        customer = Customer.objects.get(user=user)

        form = ReplayForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.user = customer #to save replay form user to customer
            test.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('customerloginview')



    return render(request, "Customerbase/feedback.html", {"form": form})
@login_required(login_url='login_user')
def feedback_replay(request):
    user=request.user
    customer_id=Customer.objects.get(user=user)
    feedback=Feedback.objects.filter(user=customer_id)

    return render(request,'Customerbase/feedback_replay.html',{'feedback':feedback})
@login_required(login_url='login_user')
def Product_search(request):
    search_product = request.GET.get('search_query')
    print(search_product)

    if search_product:
            match_product = Product_s.objects.filter(product_name=search_product)
            if match_product.exists():
                return render(request, 'Customerbase/productview.html', {'product': match_product})
            else:

                return render(request, 'Customerbase/productview.html', {'product': [],'message': 'No matching product found'})

    else:
        print("No search query provided.")


