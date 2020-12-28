from django.shortcuts import render,redirect
from user.models import User
from user.forms import UserForm
# Create your views here.
def index(request):
    print(request.method)
    if(request.method=="POST"):
        page=int(request.POST['page'])

        if('prev' in request.POST):
            page=page-1

        if('next' in request.POST):
            page=page+1

        tempOffSet=page-1
        offset=tempOffSet*4
        print(offset)

    else:
        offset=0
        page=1

    users=User.objects.raw("select * from users limit 4 offset %s",[offset])
    pageItem=len(users)
    return render(request,"user/index.html",{'users':users,'page':page,'pageItem':pageItem})

def search(request):
    print(request.POST['search'])
    user=User.objects.get(email=request.POST['search'])
    return render(request,"user/search.html",{'user':user})

def create(request):
    print(request.POST)
    if request.method=="POST":
        form=UserForm(request.POST)
        form.save()
        return redirect("/user")
    else:
        form=UserForm()
    return render(request,"user/create.html",{'form':form})

def update(request,id):
    user=User.objects.get(user_id=id)
    if request.method=="POST":
        form=UserForm(request.POST,instance=user)
        form.save()
        return redirect("/user")
    else:
        form=UserForm(instance=user)
    return render(request,"user/edit.html",{'form':form})

def delete(request,id):
    user=User.objects.get(user_id=id)
    user.delete()
    return redirect("/user")