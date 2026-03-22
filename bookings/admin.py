from django.contrib import admin
from .models import Booking
from .models import Review

admin.site.register(Booking)

admin.site.register(Review)