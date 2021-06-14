from django.contrib import admin
from .models import *


admin.site.register(MedicineName)
admin.site.register(MedicineType)
admin.site.register(MedicineInfo)
admin.site.register(GiveMedicineToPatient)
