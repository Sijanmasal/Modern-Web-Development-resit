from django.shortcuts import render
from book.models import Book
from customer.forms import CustomerForm
from book.forms import BookForm
# Create your views here.
def index(request):
    book=Book.objects.all()
    return render(request,"book/index.html",{'book':book})
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=BookForm(request.POST)
        form.save()
        form_a = CustomerForm(request.POST)
        form_a.save()
        return redirect("/book")
    else:
        form=BookForm()
    return render(request,"book/create.html",{'form':form})
def search(request):
    print(request.POST['search'])
    book=Book.objects.get(email=request.POST['search'])
    return render(request,"book/search.html",{'book':book})

def update(request,id):
    book=Book.objects.get(book_id=id)
    if request.method=="POST":
        form=BookForm(request.POST,instance=book)
        form.save()
        return redirect("/book")
    else:
        form=BookForm(instance=book)
    return render(request,"book/edit.html",{'form':form})

def delete(request,id):
    book=Book.objects.get(book_id=id)
    book.delete()
    return redirect("/book")