from django.contrib import admin
from .models import Booking,MenuItem
from rest_framework.authtoken.models import Token

# Register your models here.

admin.site.register(Booking)
admin.site.register(MenuItem)
admin.site.register(Token)
