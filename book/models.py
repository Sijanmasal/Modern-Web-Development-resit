from django.db import models
from room.models import Room
from customer.models import Customer
# Create your models here.
class Book(models.Model):
    book_id = models.AutoField(auto_created=True, primary_key=True)
    room = models.ForeignKey(Room,on_delete = models.CASCADE,)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = "book"
