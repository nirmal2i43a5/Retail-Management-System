from django.shortcuts import render,redirect
from django.http import request
# from django.contrib.auth.decorators import login_required

from customers.models import Customer
from orders.models import Order

from .forms import CustomerForm,CustomerModelForm

def create(request):
    
    form=CustomerForm()
     
    if(request.method=='POST'):
        form=CustomerForm(request.POST)#form post ma show hunxa 
        if(form.is_valid()):
            customer=Customer()
            customer.first_name=form.cleaned_data['first_name']
            customer.last_name=form.cleaned_data['last_name']
            customer.email=form.cleaned_data['email']
            customer.contact=form.cleaned_data['contact']   
            customer.status=form.cleaned_data['status']
            customer.save()
        return redirect('/customers/list?success')
            
    return render(request,'customers/create.html',{'form':form})#first ma yo page dekhinxa


def index(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    total_orders=orders.count()
    pending=orders.filter(status='Pending').count()
    delivered=orders.filter(status="Delivered").count()
    context={
        'customers':customers,'orders':orders,'total_orders':total_orders,
        'orders_pending':pending,'orders_delivered':delivered
        }
    return render(request,'customers/index.html',context)


# @login_required(login_url="/admin/login")



def edit(request, pk):    
    cus=Customer.objects.get(id=pk) 
    form=CustomerModelForm(instance=cus)
    if(request.method=='POST'):
        form=CustomerModelForm(request.POST,instance=cus)
        if(form.is_valid()):
            form.save()
        return redirect('/customers/list/?edited-successfully')#maila update.html ko save garda or post ma jada yo url ma redirect hunxa
    
    context={'form':form}
    return render(request,'customers/update.html',context)


def delete(request, pk):
    cus=Customer.objects.get(id=pk)
    
    # print(f'I am instance of {{cus}}')
    context={'name':cus }
    if request.method=='POST':  #if i confirm in delete.html page
        cus.delete()   #grab customer details and delete and return to home page
        return redirect('/customers?deleted-successfully')
    
    return render(request,'customers/delete.html',context)#urls.py ko url render ma url search garxa at first




