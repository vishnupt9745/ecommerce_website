from django.shortcuts import render, redirect, get_object_or_404

from TailWag_Supply_app.forms import LoginRegister, CustomerForm
from TailWag_Supply_app.models import Product_s, Customer, CartItem, BuyNow


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


#customer view on product
def Productview(request):
    category = request.GET.get('category')
    print(category)
    if category:
        prod = Product_s.objects.filter(product_category=category)
    else:
        prod = Product_s.objects.all()
    print(prod)

    return render(request, 'Customerbase/productview.html', {'product': prod})

def add_to_cart(request, id):
    # Try to get the selected product
    customer=Customer.objects.get(user=request.user)
    try:
        product = Product_s.objects.get(id=id)
    except Product_s.DoesNotExist:
        return redirect('productview_customer')  # Or a custom page if the product doesn't exist

    # Try to find the cart item for this product and user
    try:
        cart_item = CartItem.objects.get(product=product, user=customer)
        cart_item.quantity += 1  # Increase quantity if already in cart
    except CartItem.DoesNotExist:
        cart_item = CartItem(product=product, user=customer, quantity=1)  # Create new cart item

    cart_item.save()

    return redirect('productview_customer')

def view_cart(request):
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return redirect('productview_customer')  # If customer doesn't exist, redirect to customer view

    # Fetch all cart items for this customer
    cart_items = CartItem.objects.filter(user=customer)

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



def quantity_increase(request,id):

    increase=CartItem.objects.get(id=id)
    increase.quantity =increase.quantity +1
    increase.save()

    return redirect('cart')


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


def Buy_now(request,id):
    buy_data=Product_s.objects.get(id=id)
    customer=Customer.objects.get(user=request.user)

    if request.method =="POST":
        address = request.POST['address']
        phone = request.POST['phone']
        state = request.POST['state']
        pincode = request.POST['pincode']


    BuyNow.objects.create(
        customer=customer,            # Link the order to the logged-in customer
        product=buy_data,              # The product being bought
        quantity=1,                   # Default quantity
        address=customer.customer_address,  # Auto-fill
        phone=customer.customer_pnumber ,  # Auto-fill
        state=state,
        pincode=pincode
    )

    return render(request,'Customerbase/buy_now.html',{'buydata':buy_data,'customer':customer})


