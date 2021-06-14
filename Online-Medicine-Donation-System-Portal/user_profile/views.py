from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .forms import DonorMedicineInfoForm, RegistrationForm, MakeAppointmentForm, GivePrescriptionForm
from super_admin.models import MedicineInfo
from user_profile.forms import UserUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()


def base(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        username = user[0].username
        user_authentication = authenticate(request, username=username, password=password)
        if user_authentication is not None:
            auth_login(request, user_authentication)
            if user_authentication.is_superuser:
                return redirect(reverse('super_admin_home'))
            elif user_authentication.is_agent:
                return redirect(reverse('agent_home'))
            elif user_authentication.is_donor:
                return redirect(reverse('base'))
            else:
                return redirect(reverse('base'))
        else:
            message = "Your email And Password Is Wrong"
            context = {
                'message': message,
            }
            return render(request, 'login.html', context=context)
    if request.method == "GET":
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('base')


def donor_registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))

    if request.method == "GET":
        context = {
            'form': form
        }
        return render(request, 'donor_sign_up.html', context=context)


def create_donor_give_medicine_info(request):
    form = DonorMedicineInfoForm()
    if request.method == 'POST':
        form = DonorMedicineInfoForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.username = request.user
            m.save()
            return redirect('base')
    context = {
        'form': form
    }
    return render(request, 'Donor/GiveMedicineInfo/create_give_medicine_info.html', context=context)


def list_donor_give_medicine_info(request):
    donor_medicine_info = MedicineInfo.objects.filter(username=request.user)
    page = request.GET.get('page', 1)
    paginator = Paginator(donor_medicine_info, 5)
    try:
        donor_medicine_info = paginator.page(page)
    except PageNotAnInteger:
        donor_medicine_info = paginator.page(1)
    except EmptyPage:
        donor_medicine_info = paginator.page(paginator.num_pages)
    context = {
        'donor_medicine_info': donor_medicine_info
    }
    return render(request, 'Donor/GiveMedicineInfo/list_give_medicine_info.html', context=context)


def create_make_appointment(request):
    form = MakeAppointmentForm()
    if request.method == 'POST':
        form = MakeAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    context = {
        'form': form
    }
    return render(request, 'create_make_appointment.html', context=context)


def doctor_list_make_appointment_info(request):
    appointment = MakeAppointment.objects.filter(doctor=request.user)
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
    return render(request, 'Doctor/MakeAppointment/list_make_appointment.html', context=context)


def doctor_give_prescription(request, patient_id):
    patient = MakeAppointment.objects.get(id=patient_id)
    form = GivePrescriptionForm()
    if request.POST:
        form = GivePrescriptionForm(request.POST or None)
        if form.is_valid():
            p = form.save(commit=False)
            p.patient_name = patient
            p.doctor_name = request.user
            p.save()
            return redirect(doctor_list_make_appointment_info)
    context = {
        'form': form,
        'patient': patient
    }
    return render(request, 'Doctor/GivePrescription/create_prescription.html', context=context)


def doctor_is_check_status_change(request, patient_id):
    patient = MakeAppointment.objects.get(id=patient_id)
    print(patient)
    patient.is_check = True
    patient.save()
    return redirect('doctor_list_make_appointment_info')


def doctor_view_prescription(request, patient_id):
    patient = GivePrescription.objects.filter(patient_name=patient_id)
    context = {
        'patient': patient
    }
    return render(request, 'Doctor/GivePrescription/list_prescription.html', context=context)


def doctor_update_prescription(request, patient_id):
    patient = GivePrescription.objects.get(id=patient_id)
    print(patient)
    form = GivePrescriptionForm(instance=patient)
    if request.method == "POST":
        form = GivePrescriptionForm(request.POST or None, instance=patient)
        if form.is_valid():
            form.save()
            return redirect(doctor_list_make_appointment_info)
    context = {
        'form': form
    }
    return render(request, 'Doctor/GivePrescription/update_prescription.html', context=context)


def doctor_list(request):
    doctor = User.objects.filter(is_doctor=True)
    context = {
        'doctor': doctor
    }
    return render(request, 'doctor_list.html', context=context)


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        con = Contact()
        con.name = name
        con.email = email
        con.subject = subject
        con.message = message
        con.save()
        return redirect('base')
    else:
        return render(request, 'contact.html')


def patient_list_make_appointment_info(request):
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
    return render(request, 'list_make_appointment.html', context=context)


def profile(request):
    return render(request, 'Profile/profile.html')


def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'Profile/update_profile.html', context=context)


def user_password_change(request):
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
        return render(request, 'Profile/password_change.html', context=context)
