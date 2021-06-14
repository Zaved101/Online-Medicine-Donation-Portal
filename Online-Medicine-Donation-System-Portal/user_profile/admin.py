from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'email', 'is_donor',  'is_doctor', 'is_agent', 'is_superuser')


admin.site.register(User, UserAdmin)
admin.site.register(MakeAppointment)
admin.site.register(GivePrescription)
admin.site.register(Contact)

