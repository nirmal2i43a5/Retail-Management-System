


from django import forms

from django.forms import ModelForm

from .models import Product


    
   
class ProductModelForm(ModelForm):
    class Meta:
        model=Product
        fields=['name','price','category','description']