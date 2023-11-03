from django.db import models
# Create your models here.
class Booking(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    no_of_guests = models.IntegerField()
    #booking_date = models.DateTimeField(default=datetime.today())

class Menu(models.Model):
    id = models.URLField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()