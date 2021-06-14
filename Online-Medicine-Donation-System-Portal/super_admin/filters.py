import django_filters
from .models import *


class MedicineInfoFilter(django_filters.FilterSet):
    class Meta:
        model = MedicineInfo
        fields = ['medicine_name', 'medicine_type']
