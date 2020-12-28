from django.shortcuts import render,redirect
from customer.models import Customer
from customer.forms import CustomerForm
# Create your views here.
def index(request):
    customers=Customer.objects.all()
    return render(request,"customer/index.html",{'customers':customers})

def create(request):
    print(request.POST)
    if request.method=="POST":
        form=CustomerForm(request.POST)
        form.save()
        return redirect("/customer")
    else:
        form=CustomerForm()
    return render(request,"customer/create.html",{'form':form})

def update(request,id):
    customer=Customer.objects.get(customer_id=id)
    if request.method=="POST":
        form=CustomerForm(request.POST,instance=customer)
        form.save()
        return redirect("/customer")
    else:
        form=CustomerForm(instance=customer)
    return render(request,"customer/edit.html",{'form':form})

def delete(request,id):
    customer=Customer.objects.get(customer_id=id)
    customer.delete()
    return redirect("/customer")