from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class DoctorForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    email = forms.EmailField(label=_('Email'), help_text=_('Required. Enter an existing email address.'), required=True)
    phone_number = forms.CharField(label=_('Phone Number'), help_text=_('Required. Enter an existing Email Number .'
                                                                        'plz enter 01...'),
                                   required=True)

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))

        return email


class AgentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    email = forms.EmailField(label=_('Email'), help_text=_('Required. Enter an existing email address.'), required=True)
    phone_number = forms.CharField(label=_('Phone Number'), help_text=_('Required. Enter an existing Email Number .'
                                                                        'plz enter 01...'),
                                   required=True)

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))

        return email


class MedicineNameForm(forms.ModelForm):
    class Meta:
        model = MedicineName
        fields = ['medicine_name']


class MedicineTypeForm(forms.ModelForm):
    class Meta:
        model = MedicineType
        fields = ['medicine_type']


class MedicineInfoForm(forms.ModelForm):
    expiry_date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    class Meta:
        model = MedicineInfo
        fields = ['medicine_name', 'medicine_type', 'number_of_medicine', 'mg', 'expiry_date']


class GivePrescriptionToPatientForm(forms.ModelForm):

    class Meta:
        model = GiveMedicineToPatient
        fields = ['patient_name', 'give_number_of_medicine']
