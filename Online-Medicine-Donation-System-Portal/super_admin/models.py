from django.db import models
from django.conf import settings
import pytz
from datetime import date


class MedicineName(models.Model):
    medicine_name = models.CharField(max_length=100)

    def __str__(self):
        return self.medicine_name


class MedicineType(models.Model):
    medicine_type = models.CharField(max_length=100)

    def __str__(self):
        return self.medicine_type


class MedicineInfo(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medicine_name = models.ForeignKey(MedicineName, on_delete=models.CASCADE)
    medicine_type = models.ForeignKey(MedicineType, on_delete=models.CASCADE)
    number_of_medicine = models.IntegerField(verbose_name='Number of Medicine')
    mg = models.CharField(max_length=20, verbose_name='Medicine MG')
    expiry_date = models.DateField(verbose_name='Medicine Expiry Date')
    location = models.TextField(null=True, blank=True, verbose_name='Donor Location')
    is_collected = models.BooleanField(null=True, blank=True, verbose_name='Agent Collected')

    def __str__(self):
        return str(self.username)


class GiveMedicineToPatient(models.Model):
    medicine = models.ForeignKey(MedicineInfo, on_delete=models.CASCADE)
    patient_name = models.ForeignKey('user_profile.MakeAppointment', on_delete=models.CASCADE)
    give_number_of_medicine = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.patient_name)
