from django import forms
from .models import OrderCL,CustomerCL

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderCL
        fields = ['customer', 'products']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerCL
        fields = ['username', 'email', 'full_name']
