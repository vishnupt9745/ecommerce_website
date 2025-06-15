from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

from TailWag_Supply_app.models import Login, Seller, Customer, Product_s, Buynow_data, Feedback


class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirmpassword", widget=forms.PasswordInput)

    class Meta:
        model=Login
        fields=('username','password1','password2')

class SellerForm(forms.ModelForm):
    class Meta:
        model=Seller
        fields='__all__'
        exclude=('user','seller_id',)



class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=('user','customer_id',)

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product_s
        fields='__all__'
        exclude=('product_user',)

class BuynowForm(forms.ModelForm):
    class Meta:
        model=Buynow_data
        fields='__all__'
        exclude=('seller','customer','product','product_img','choice','expected_date ')

class BuynowStatus(forms.ModelForm):
    expected_date = forms.DateField(widget=DateInput)
    class Meta:
        model=Buynow_data
        fields='__all__'
        exclude = ('seller', 'customer','product','quantity','address','state','pincode','phone','is_paid','order_date',)


class ReplayForm(forms.ModelForm):

    class Meta:
        model=Feedback
        fields='__all__'
        exclude=('user','replay',)