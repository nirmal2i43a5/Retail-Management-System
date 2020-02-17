



from django import forms
from django.forms import ModelForm
from .models import Customer

class CustomerForm(forms.Form):
    first_name=forms.CharField(max_length=50,required=True)
    last_name=forms.CharField(max_length=50,required=True)
    email=forms.CharField(max_length=50,required=True)
    contact=forms.CharField(max_length=50,required=True)
    
    status=forms.BooleanField(required=False)
    
    
class CustomerModelForm(ModelForm):
    class Meta:
        model=Customer
        fields=['first_name','last_name','email','contact']
        
 
 
 
    
        
        
     
        

    
    
    
    
    
    
    
    