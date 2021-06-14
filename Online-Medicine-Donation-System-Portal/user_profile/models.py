from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.contrib.auth.models import User
from django.conf import settings
from super_admin.models import *


class User(AbstractUser):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    is_agent = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='profile_pics')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class MakeAppointment(models.Model):
    name = models.CharField(max_length=154, verbose_name='Your Name')
    email = models.EmailField(verbose_name='Your Email')
    phone = models.CharField(max_length=15, verbose_name='Your Phone')
    date = models.DateField(verbose_name='Appointment Date')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               limit_choices_to={'is_doctor': True},
                               verbose_name='Doctor Name')
    message = models.TextField()
    is_check = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name


class GivePrescription(models.Model):
    patient_name = models.ForeignKey(MakeAppointment, on_delete=models.CASCADE)
    doctor_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medicine_name = models.ForeignKey(MedicineName, on_delete=models.CASCADE, verbose_name=' Medicine Name')
    medicine_type = models.ForeignKey(MedicineType, on_delete=models.CASCADE, verbose_name=' Medicine Type')
    day_of_medicine = models.IntegerField(verbose_name='Day Of Medicine')
    morning = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)

    def __str__(self):
        return str(self.patient_name)


class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
