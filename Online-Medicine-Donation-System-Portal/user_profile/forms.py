from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from super_admin.models import *
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'phone_number', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_donor = True
        user.save()
        return user

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        user = User.objects.filter(phone_number__iexact=phone_number).exists()
        if user:
            raise ValidationError(_('You can not use this Phone Number.'))

        return phone_number

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))
        return email


class DonorMedicineInfoForm(forms.ModelForm):
    expiry_date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    class Meta:
        model = MedicineInfo
        fields = ['medicine_name', 'medicine_type', 'number_of_medicine', 'mg', 'expiry_date', 'location']


class MakeAppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    class Meta:
        model = MakeAppointment
        fields = ['name', 'email', 'phone', 'date', 'doctor', 'message']


class GivePrescriptionForm(forms.ModelForm):
    class Meta:
        model = GivePrescription
        fields = ['medicine_name', 'medicine_type', 'day_of_medicine', 'morning', 'lunch', 'dinner']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for username in self.fields.keys():
            self.fields[username].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'address', 'image']
