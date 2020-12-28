from django.shortcuts import render,redirect
from room.models import Room
from room.forms import RoomForm
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

    room=Room.objects.raw("select * from room limit 4 offset %s",[offset])
    pageItem=len(room)
    return render(request,"room/index.html",{'room':room,'page':page,'pageItem':pageItem})

def create(request):
    print(request.POST)
    if request.method=="POST":
        form=RoomForm(request.POST,request.FILES)
        form.save()
        return redirect("/room")
    else:
        form=RoomForm()
    return render(request,"room/create.html",{'form':form})

def update(request,id):
    room=Room.objects.get(room_id=id)
    if request.method=="POST":
        form=RoomForm(request.POST,request.FILES,instance=room)
        form.save()
        return redirect("/room")
    else:
        form=RoomForm(instance=room)
    return render(request,"room/edit.html",{'form':form})

def delete(request,id):
    room=Room.objects.get(room_id=id)
    room.delete()
    return redirect("/room")