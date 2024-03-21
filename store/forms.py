from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from .models import Product, Order


class OrderForm(forms.ModelForm):
    phone_number = PhoneNumberField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city', 'phone_number']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={'class': 'w-full p-4 border border-gray-200'}),
            'title': forms.TextInput(attrs={'class': 'w-full p-4 border border-gray-200'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-4 border border-gray-200'}),
            'price': forms.NumberInput(attrs={'class': 'w-full p-4 border border-gray-200'}),
            'image': forms.FileInput(attrs={'class': 'w-full p-4 border border-gray-200'}),

        }
