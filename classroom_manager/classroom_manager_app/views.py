from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import StandardForm, DivisionForm, StaffForm, CompalaintForm, LeaveForm, LoginForm
from .models import Standard, Division, Staff, Complaint, Leave, CustomUser

# Create your views here.

def home(request):
    return render(request, 'home.html')

def admin_home(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return render(request, 'admin_home.html')

def logout_view(request):
    logout(request)
    return redirect('/')


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
        else:
            messages.info(request, 'invalid credentials')
    return render(request, 'login.html')

def add_standard(request):
    standard_form = StandardForm()
    if request.method == 'POST':
        standard_form = StandardForm(request.POST)
        if standard_form.is_valid:
            standard = standard_form.save()
            standard.save()
            messages.info(request, 'Standard Added Successful')
            return redirect('standard_view')
    return render(request, 'add_standard.html', {'standard_form': standard_form})


def standard_view(request):
    standard = Standard.objects.all()
    return render(request, 'standard_view.html', {'standard': standard})

def standard_delete(request, id):
    data = Standard.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('standard_view')
    else:
        return redirect('standard_view')
    
def add_divsion(request):
    division_form = DivisionForm()
    if request.method == 'POST':
        division_form = DivisionForm(request.POST)
        if division_form.is_valid:
            divsion = division_form.save()
            divsion.save()
            messages.info(request, 'Division Added Successful')
            return redirect('division_view')
    return render(request, 'add_division.html', {'division_form': division_form})


def division_view(request):
    division = Division.objects.all()
    return render(request, 'division_view.html', {'division': division})

def division_delete(request, id):
    data = Division.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('division_view')
    else:
        return redirect('division_view')
    

def staff_register(request):
    login_form = LoginForm()
    staff_form = StaffForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        staff_form = StaffForm(request.POST)
        if login_form.is_valid() and staff_form.is_valid():
            user = login_form.save(commit=False)
            user.user_type = 'staff'
            user.save()
            staff = staff_form.save(commit=False)
            staff.user = user
            staff.save()
            messages.info(request, 'Staff Registered Successful')
            return redirect('staff_view')
    return render(request, 'register_staff.html', {'login_form': login_form, 'staff_form': staff_form})


def staff_view(request):
    staff = Staff.objects.all()
    return render(request, 'staff_view.html ', {'staff': staff})


def staff_delete(request, id):
    data = Staff.objects.get(id=id)
    if request.method == "POST":
        data.delete()
        data.user.delete()
        return redirect('staff_view')
    else:
        return redirect('staff_view')
