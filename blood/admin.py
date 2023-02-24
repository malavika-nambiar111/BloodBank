from django.contrib import admin

from .models import Patient, Contact, Donor

# Register your models here

admin.site.register(Patient)

admin.site.register(Donor)

class customerdetails(admin.ModelAdmin):
    list_display=('name','phno','email')
admin.site.register(Contact,customerdetails)