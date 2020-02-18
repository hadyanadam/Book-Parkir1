from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Parkir(models.Model):
    # name = models.CharField(max_length = 15)
    # id = models.AutoField()
    user = models.CharField(max_length=20, null=True, blank=True)
    booking_place = models.CharField(max_length= 10)
    book_status = models.BooleanField(null=True)
    def __str__(self):
        return "{}. {}. {}".format(self.booking_place, self.user, self.book_status)
    
class Saldo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    saldo = models.IntegerField(default = 100000)
    def __str__(self):
        return f"Rp. {self.saldo}"
    
class DeadlineParkir(models.Model):
    id = models.AutoField(primary_key=True)
    parkir = models.OneToOneField(Parkir, on_delete=models.CASCADE, null= True)
    deadline = models.CharField(max_length=30,null=True)
    def __str__(self):
        return f"{self.deadline}"