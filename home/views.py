from django.shortcuts import render,redirect
from room.models import Room
from customer.forms import CustomerForm
from room.forms import RoomForm
# Create your views here.
def index(request):
    room=Room.objects.all()
    return render(request,'home/index.html' ,{'room':room})
def register(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        result=form.save()
        request.session['customer_id']=result.customer_id
        return redirect("/")
    else:
        form=CustomerForm()
    return render(request,"home/register.html",{'form':form})
def login(request):
    if(request.method=='POST'):
       request.session['email']=request.POST['email']
       request.session['password']=request.POST['password']
       return redirect("/user")
    return render(request,"home/login.html")
def logout(request):
    request.session.clear()
    return redirect("/")
def about(request):
    room = Room.objects.all()
    return render(request, 'home/about.html', {'room': room})
def accomodation(request):
    room = Room.objects.all()
    return render(request, 'home/accomodation.html', {'room': room})
def blog(request):
    room = Room.objects.all()
    return render(request, 'home/blog.html', {'room': room})
def blog_single(request):
    room = Room.objects.all()
    return render(request, 'home/blog-single.html', {'room': room})
def contact(request):
    room = Room.objects.all()
    return render(request, 'home/contact.html', {'room': room})
def elements(request):
    room = Room.objects.all()
    return render(request, 'home/elements.html', {'room': room})
def gallery(request):
    room = Room.objects.all()
    return render(request, 'home/gallery.html', {'room': room})
