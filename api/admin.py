from django.contrib import admin
from .models import Parkir, Saldo, DeadlineParkir, BookingTime

# Register your models here.
admin.site.register(Parkir)
admin.site.register(Saldo)
admin.site.register(DeadlineParkir)
admin.site.register(BookingTime)