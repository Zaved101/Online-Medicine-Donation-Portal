from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import *
from .filters import *
from user_profile.models import *
from user_profile.forms import UserUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import get_user_model
User = get_user_model()


def super_admin_home(request):
    return render(request, 'superadmin/index.html')


def agent_home(request):
    return render(request, 'superadmin/index.html')


def list_doctor(request):
    doctor = User.objects.filter(owner=request.user, is_doctor=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(doctor, 5)
    try:
        doctor = paginator.page(page)
    except PageNotAnInteger:
        doctor = paginator.page(1)
    except EmptyPage:
        doctor = paginator.page(paginator.num_pages)

    context = {
        'doctor': doctor
    }
    return render(request, 'superadmin/Doctor/doctor_list.html', context=context)


def create_doctor(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST or None)
        if form.is_valid():
            d = form.save(commit=False)
            d.owner = request.user
            d.is_doctor = True
            d.save()
            return redirect('list_doctor')
    context = {
        'form': form
    }
    return render(request, 'superadmin/Doctor/doctor_create.html', context=context)


def view_doctor(request, pk):
    doctor = get_object_or_404(User, pk=pk)
    context = {
        'doctor': doctor
    }
    return render(request, 'superadmin/Doctor/doctor_view.html', context=context)


def delete_doctor(request, pk):
    doctor = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('list_doctor')
    context = {
        'doctor': doctor
    }
    return render(request, 'superadmin/Doctor/doctor_delete.html', context=context)


def list_agent(request):
    agent = User.objects.filter(is_agent=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(agent, 5)
    try:
        agent = paginator.page(page)
    except PageNotAnInteger:
        agent = paginator.page(1)
    except EmptyPage:
        agent = paginator.page(paginator.num_pages)

    context = {
        'agent': agent
    }
    return render(request, 'superadmin/Agent/agent_list.html', context=context)


def create_agent(request):
    form = AgentForm()
    if request.method == 'POST':
        form = AgentForm(request.POST or None)
        if form.is_valid():
            d = form.save(commit=False)
            d.is_agent = True
            d.save()
            return redirect('list_agent')
    context = {
        'form': form
    }
    return render(request, 'superadmin/Agent/agent_create.html', context=context)


def view_agent(request, pk):
    agent = get_object_or_404(User, pk=pk)
    context = {
        'agent': agent
    }
    return render(request, 'superadmin/Agent/agent_view.html', context=context)


def delete_agent(request, pk):
    agent = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        agent.delete()
        return redirect('list_doctor')
    context = {
        'agent': agent
    }
    return render(request, 'superadmin/Agent/agent_delete.html', context=context)


def list_medicine_name(request):
    medicine_name = MedicineName.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(medicine_name, 5)
    try:
        medicine_name = paginator.page(page)
    except PageNotAnInteger:
        medicine_name = paginator.page(1)
    except EmptyPage:
        medicine_name = paginator.page(paginator.num_pages)
    context = {
        'medicine_name': medicine_name
    }
    return render(request, 'superadmin/MedicineName/list_medicine_name.html', context=context)


def create_medicine_name(request):
    form = MedicineNameForm()
    if request.method == 'POST':
        form = MedicineNameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_medicine_name')
    context = {
        'form': form
    }
    return render(request, 'superadmin/MedicineName/create_medicine_name.html', context=context)


def update_medicine_name(request, medicine_name_id):
    medicine_name = MedicineName.objects.get(id=medicine_name_id)
    print(medicine_name)
    form = MedicineNameForm(instance=medicine_name)
    if request.method == "POST":
        form = MedicineNameForm(request.POST, instance=medicine_name)
        if form.is_valid():
            form.save()
            return redirect('list_medicine_name')
    context = {
        'form': form
    }
    return render(request, 'superadmin/MedicineName/update_medicine_name.html', context=context)


def delete_medicine_name(request, medicine_name_id):
    medicine_name = MedicineName.objects.get(id=medicine_name_id)
    if request.method == 'POST':
        medicine_name.delete()
        return redirect('list_medicine_name')
    context = {
        'medicine_name': medicine_name
    }
    return render(request, 'superadmin/MedicineName/delete_medicine_name.html', context=context)


def list_medicine_type(request):
    medicine_type = MedicineType.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(medicine_type, 5)
    try:
        medicine_type = paginator.page(page)
    except PageNotAnInteger:
        medicine_type = paginator.page(1)
    except EmptyPage:
        medicine_type = paginator.page(paginator.num_pages)
    context = {
        'medicine_type': medicine_type
    }
    return render(request, 'superadmin/MedicineType/list_medicine_type.html', context=context)


def create_medicine_type(request):
    form = MedicineTypeForm()
    if request.method == 'POST':
        form = MedicineTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_medicine_type')
    context = {
        'form': form
    }
    return render(request, 'superadmin/MedicineType/create_medicine_type.html', context=context)


def update_medicine_type(request, medicine_type_id):
    medicine_type = MedicineType.objects.get(id=medicine_type_id)
    form = MedicineTypeForm(instance=medicine_type)
    if request.method == "POST":
        form = MedicineTypeForm(request.POST, instance=medicine_type)
        if form.is_valid():
            form.save()
            return redirect('list_medicine_type')
    context = {
        'form': form
    }
    return render(request, 'superadmin/MedicineType/update_medicine_type.html', context=context)


def delete_medicine_type(request, medicine_type_id):
    medicine_type = MedicineType.objects.get(id=medicine_type_id)
    if request.method == 'POST':
        medicine_type.delete()
        return redirect('list_medicine_type')
    context = {
        'medicine_type': medicine_type
    }
    return render(request, 'superadmin/MedicineType/delete_medicine_type.html', context=context)


def list_medicine_info(request):
    now_date = date.today()
    medicine_info = MedicineInfo.objects.filter(username=request.user, expiry_date__gte=now_date)
    donor = MedicineInfo.objects.filter(username__is_donor=True, expiry_date__gte=now_date)
    page = request.GET.get('page', 1)
    paginator = Paginator(medicine_info, 5)
    paginator1 = Paginator(donor, 5)
    try:
        medicine_info = paginator.page(page)
        donor = paginator1.page(page)
    except PageNotAnInteger:
        medicine_info = paginator.page(1)
        donor = paginator1.page(1)
    except EmptyPage:
        medicine_info = paginator.page(paginator.num_pages)
        donor = paginator1.page(paginator1.num_pages)
    context = {
        'medicine_info': medicine_info,
        'donor': donor,
        'today': now_date
    }
    return render(request, 'superadmin/MedicineInfo/list_medicine_info.html', context=context)


def expiry_date_list_of_medicine_info(request):
    now_date = date.today()
    medicine_info = MedicineInfo.objects.filter(username=request.user, expiry_date__lte=now_date)
    donor = MedicineInfo.objects.filter(username__is_donor=True, expiry_date__lte=now_date)
    page = request.GET.get('page', 1)
    paginator = Paginator(medicine_info, 5)
    paginator1 = Paginator(donor, 5)
    try:
        medicine_info = paginator.page(page)
        donor = paginator1.page(page)
    except PageNotAnInteger:
        medicine_info = paginator.page(1)
        donor = paginator1.page(1)
    except EmptyPage:
        medicine_info = paginator.page(paginator.num_pages)
        donor = paginator1.page(paginator1.num_pages)
    context = {
        'medicine_info': medicine_info,
        'donor': donor,
        'today': now_date
    }

    return render(request, 'superadmin/MedicineInfo/expiry_date_medicine_info.html', context=context)


def create_medicine_info(request):
    form = MedicineInfoForm()
    if request.method == 'POST':
        form = MedicineInfoForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.username = request.user
            m.save()
            return redirect('list_medicine_info')
    context = {
        'form': form
    }
    return render(request, 'superadmin/MedicineInfo/create_medicine_info.html', context=context)


def update_medicine_info(request, medicine_info_id):
    medicine_info = MedicineInfo.objects.get(id=medicine_info_id)
    form = MedicineInfoForm(instance=medicine_info)
    if request.method == "POST":
        form = MedicineInfoForm(request.POST, instance=medicine_info)
        if form.is_valid():
            form.save()
            return redirect('list_medicine_info')
    context = {
        'form': form
    }
    return render(request, 'superadmin/MedicineInfo/update_medicine_info.html', context=context)


def delete_medicine_info(request, medicine_info_id):
    medicine_info = MedicineInfo.objects.get(id=medicine_info_id)
    if request.method == 'POST':
        medicine_info.delete()
        return redirect('list_medicine_info')
    context = {
        'medicine_info': medicine_info
    }
    return render(request, 'superadmin/MedicineInfo/delete_medicine_info.html', context=context)


# agent part
def agent_list_medicine_info(request):
    medicine_info = MedicineInfo.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(medicine_info, 5)
    try:
        medicine_info = paginator.page(page)
    except PageNotAnInteger:
        medicine_info = paginator.page(1)
    except EmptyPage:
        medicine_info = paginator.page(paginator.num_pages)
    context = {
        'medicine_info': medicine_info
    }
    return render(request, 'Agent/MedicineInfo/list_medicine_info.html', context=context)


def super_admin_list_make_appointment_info(request):
    appointment = MakeAppointment.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(appointment, 5)
    try:
        appointment = paginator.page(page)
    except PageNotAnInteger:
        appointment = paginator.page(1)
    except EmptyPage:
        appointment = paginator.page(paginator.num_pages)
    context = {
        'appointment': appointment
    }
    return render(request, 'superadmin/MakeAppointment/list_make_appointment.html', context=context)


def agent_is_collected_status_change(request, donor_id):
    medicine = MedicineInfo.objects.get(id=donor_id)
    medicine.is_collected = True
    medicine.save()
    return redirect('agent_list_medicine_info')


def view_prescription(request, patient_id):
    patient = GivePrescription.objects.filter(patient_name=patient_id)
    patient_medicine = GiveMedicineToPatient.objects.filter(patient_name=patient_id)
    now_date = date.today()
    medicine_info = MedicineInfo.objects.filter(expiry_date__gte=now_date)
    MyFilter = MedicineInfoFilter(request.GET, queryset=medicine_info)
    medicine_info = MyFilter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(medicine_info, 10)
    try:
        medicine_info = paginator.page(page)
    except PageNotAnInteger:
        medicine_info = paginator.page(1)
    except EmptyPage:
        medicine_info = paginator.page(paginator.num_pages)
    context = {
        'patient': patient,
        'patient_medicine': patient_medicine,
        'medicine_info': medicine_info,
        'MyFilter': MyFilter
    }
    return render(request, 'superadmin/GivePrescription/list_prescription.html', context=context)


def view_contact(request):
    contact = Contact.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(contact, 10)
    try:
        contact = paginator.page(page)
    except PageNotAnInteger:
        contact = paginator.page(1)
    except EmptyPage:
        contact = paginator.page(paginator.num_pages)
    context = {
        'contact': contact
    }
    return render(request, 'superadmin/contact.html', context=context)


def profile(request):
    return render(request, 'superadmin/Profile/profile.html')


def super_admin_update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'superadmin/Profile/update_profile.html', context=context)


def password_change(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('login'))
        else:
            pass
    else:
        form = PasswordForm(request.user)
        context = {
            'form': form
        }
        return render(request, 'superadmin/Profile/password_change.html', context=context)


def give_prescription_to_patient(request, medicine_id):
    medicine = MedicineInfo.objects.get(id=medicine_id)
    form = GivePrescriptionToPatientForm(instance=medicine)
    if request.method == "POST":
        medicine = MedicineInfo.objects.get(id=medicine_id)
        form = GivePrescriptionToPatientForm(request.POST)
        if form.is_valid():
            gm = form.save(commit=False)
            medicine1 = medicine
            gm.medicine = medicine1
            give_number_of_medicine = form.cleaned_data.get('give_number_of_medicine')
            medicine.number_of_medicine -= give_number_of_medicine
            medicine.save()
            gm.save()
            return redirect(reverse('super_admin_list_make_appointment_info'))
    context = {
        'form': form,
        'medicine_id': medicine_id
    }
    return render(request, 'superadmin/GivePrescription/give_medicine_to_patient.html', context=context)


def donor_list(request):
    donor = User.objects.filter(is_donor=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(donor, 10)
    try:
        donor = paginator.page(page)
    except PageNotAnInteger:
        donor = paginator.page(1)
    except EmptyPage:
        donor = paginator.page(paginator.num_pages)
    context = {
        'donor': donor
    }
    return render(request, 'superadmin/donor_list.html', context=context)
