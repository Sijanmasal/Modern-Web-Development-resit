from django.db import models

# Create your models here.
class Room(models.Model):
   room_id = models.AutoField(auto_created=True, primary_key=True)
   description = models.CharField(max_length=100)
   price = models.CharField(max_length=20,default="")
   image = models.FileField(upload_to="static/images/room/")

   class Meta:
       db_table = "room"
