from django.urls import path
from .views import *


urlpatterns = [
    path('super/admin/home/', super_admin_home, name="super_admin_home"),

    path('doctor/list/', list_doctor, name='list_doctor'),
    path('doctor/create/', create_doctor, name='create_doctor'),
    path('doctor/view/<int:pk>/', view_doctor, name='view_doctor'),
    path('doctor/delete/<int:pk>/', delete_doctor, name='delete_doctor'),

    path('agent/list/', list_agent, name='list_agent'),
    path('agent/create/', create_agent, name='create_agent'),
    path('agent/view/<int:pk>/', view_agent, name='view_agent'),
    path('agent/delete/<int:pk>/', delete_agent, name='delete_agent'),

    path('medicine/name/create/', create_medicine_name, name='create_medicine_name'),
    path('medicine/name/list/', list_medicine_name, name='list_medicine_name'),
    path('medicine/name/update/<int:medicine_name_id>/', update_medicine_name, name='update_medicine_name'),
    path('medicine/name/delete/<int:medicine_name_id>/', delete_medicine_name, name='delete_medicine_name'),

    path('medicine/type/list/', list_medicine_type, name='list_medicine_type'),
    path('medicine/type/create/', create_medicine_type, name='create_medicine_type'),
    path('medicine/type/update/<int:medicine_type_id>/', update_medicine_type, name='update_medicine_type'),
    path('medicine/type/delete/<int:medicine_type_id>/', delete_medicine_type, name='delete_medicine_type'),

    path('medicine/info/list/', list_medicine_info, name='list_medicine_info'),
    path('medicine/info/create/', create_medicine_info, name='create_medicine_info'),
    path('medicine/info/update/<int:medicine_info_id>/', update_medicine_info, name='update_medicine_info'),
    path('medicine/info/delete/<int:medicine_info_id>/', delete_medicine_info, name='delete_medicine_info'),

    path('super_admin_list_make_appointment_info', super_admin_list_make_appointment_info,
         name='super_admin_list_make_appointment_info'),

    path('view/contact/', view_contact, name='view_contact'),
    path('profile/', profile, name='profile'),
    path('super_admin_update_profile/', super_admin_update_profile, name='super_admin_update_profile'),
    path('change_password/', password_change, name='change_password'),

    path('view_prescription/<int:patient_id>/', view_prescription, name='view_prescription'),
    path('give_prescription_to_patient/<int:medicine_id>/', give_prescription_to_patient,
         name='give_prescription_to_patient'),

    path('donor_list', donor_list, name='donor_list'),
    # agent
    path('agent/home/', agent_home, name="agent_home"),
    path('agent/medicine/info/list/', agent_list_medicine_info, name='agent_list_medicine_info'),
    path('agent/medicine/info/is/collected/<int:donor_id>/', agent_is_collected_status_change,
         name='agent_is_collected_status_change'),

    path('expiry_date_list_of_medicine_info/', expiry_date_list_of_medicine_info,
         name='expiry_date_list_of_medicine_info'),
]
