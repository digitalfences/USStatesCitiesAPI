from django.contrib import admin

# Register your models here.
from .models import Location, State, Country

admin.site.register(Location)
admin.site.register(State)
admin.site.register(Country)