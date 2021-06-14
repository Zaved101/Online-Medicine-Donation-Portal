from django.urls import path
from .views import *


urlpatterns = [
    path('', base, name='base'),
    path('login/', login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('donor_registration/', donor_registration, name='donor_registration'),
    path('doctor/list/', doctor_list, name='doctor_list'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('contact/', contact, name='contact'),
    path('profile/', profile, name='user_profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('user_password_change/', user_password_change, name='user_password_change'),



    # donor
    path('create_donor_give_medicine_info/', create_donor_give_medicine_info, name='create_donor_give_medicine_info'),
    path('list_donor_give_medicine_info/', list_donor_give_medicine_info, name='list_donor_give_medicine_info'),


    path('create_make_appointment/', create_make_appointment, name='create_make_appointment'),

    # doctor
    path('doctor_list_make_appointment_info/', doctor_list_make_appointment_info,
         name='doctor_list_make_appointment_info'),
    path('doctor_give_prescription/<int:patient_id>/', doctor_give_prescription, name='doctor_give_prescription'),
    path('doctor_is_check_status_change/<int:patient_id>/', doctor_is_check_status_change,
         name='doctor_is_check_status_change'),
    path('doctor_view_prescription/<int:patient_id>/', doctor_view_prescription,
         name='doctor_view_prescription'),
    path('doctor_update_prescription/<int:patient_id>/', doctor_update_prescription,
         name='doctor_update_prescription'),

    path('patient_list_make_appointment_info', patient_list_make_appointment_info,
         name='patient_list_make_appointment_info'),

]
