from django import forms
from .models import Order, Review

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'products', 'date', 'total_amount']

        widgets = {
            'products': forms.CheckboxSelectMultiple,  # Assuming multiple products can be selected
            'date': forms.DateInput(attrs={'type': 'date'})  # Use a date picker in the form
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'rating', 'comment']

        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5})  # Restrict rating to a range of 1-5
        }
