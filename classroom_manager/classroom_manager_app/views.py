from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import StandardForm, DivisionForm, StaffForm, CompalaintForm, LeaveForm, LoginForm, StudentForm, AttendanceForm
from .models import Standard, Division, Staff, Complaint, Leave, CustomUser, Student, Attandance
import datetime
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def admin_home(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return render(request, 'admin_home.html')

def staff_home(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return render(request, 'staff_home.html')

def student_home(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return render(request, 'student_home.html')

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
            if user.user_type == "staff":
                return redirect('staff_home')
            if user.user_type == "student":
                return redirect('student_home')
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

def standard_view_staff(request):
    standard = Standard.objects.all()
    return render(request, 'standard_view_staff.html', {'standard': standard})

def division_view_staff(request):
    division = Division.objects.all()
    return render(request, 'division_view_staff.html', {'division': division})

def staff_view_for_staff(request):
    staff = Staff.objects.all()
    return render(request, 'staff_view_for_staff.html ', {'staff': staff})

def staff_view_for_student(request):
    staff = Staff.objects.all()
    return render(request, 'staff_view_for_student.html ', {'staff': staff})

def student_register(request):
    login_form = LoginForm()
    staff_form = StudentForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        staff_form = StudentForm(request.POST)
        if login_form.is_valid() and staff_form.is_valid():
            user = login_form.save(commit=False)
            user.user_type = 'student'
            user.save()
            staff = staff_form.save(commit=False)
            staff.user = user
            staff.save()
            messages.info(request, 'Student Registered Successful')
            return redirect('student_view_admin')
    return render(request, 'register_student.html', {'login_form': login_form, 'staff_form': staff_form})

def student_view_for_staff(request):
    staff = Student.objects.all()
    return render(request, 'student_view_for_staff.html ', {'staff': staff})

def student_view_for_admin(request):
    staff = Student.objects.all()
    return render(request, 'student_view_for_admin.html ', {'staff': staff})

now = datetime.datetime.now()

def mark_attendance(request, id):
    user = Student.objects.get(id=id)
    add = Attandance.objects.filter(student=user, date=datetime.date.today())
    if add.exists():
        messages.info(request, f"{user}'s Today's Attendance is already Marked!")
        return redirect('add_attendance')
    else:
        if request.method == 'POST':
            status = request.POST.get('status')
            Attandance(student=user, date=datetime.date.today(), status=status, division=user.division).save()
            messages.info(request, "Attendance added Succesfully")
            return redirect('add_attendance')
        return render(request, 'mark_attendance.html')


def add_attendance(request):
    students = Student.objects.all()
    return render(request, 'add_attendance.html', {'students': students})


def attendance_view_for_student(request, id):
    print(">>", id)
    user = request.user
    attendance = Attandance.objects.filter(student__user=id).order_by('-date')
    p = attendance.filter(status='present').count()
    a = attendance.filter(status='absent').count()
    return render(request, 'attendance_view_for_stud.html ', {'attendance': attendance, 'user': user, 'a':a, 'p':p})


def add_leave(request):
    leaveform = LeaveForm()
    if request.method == 'POST':
        leaveform = LeaveForm(request.POST)
        if leaveform.is_valid:
            leave = leaveform.save(commit=False)
            student = Student.objects.get(user=request.user)
            leave.student = student
            leave.division = student.division
            leave.save()
            messages.info(request, 'Leave Added Successful')
            return redirect(reverse('leave_view_for_stud', kwargs={'id': request.user.id}))
    return render(request, 'add_leave.html', {'leaveform': leaveform})


def leave_view_for_stud(request, id):
    leave = Leave.objects.filter(student__user=id).order_by('-date')
    return render(request, 'leave_view_for_stud.html', {'leave': leave})

def leave_delete(request, id):
    data = Leave.objects.get(id=id)
    if request.method == 'POST':
        print("pppppp")
        data.delete()
        print("qqqqqqq")
        return redirect(reverse('leave_view_for_stud', kwargs={'id': request.user.id}))
    else:
        return redirect(reverse('leave_view_for_stud', kwargs={'id': request.user.id}))
    

def add_complaint(request):
    complaint_form = CompalaintForm()
    if request.method == 'POST':
        complaint_form = CompalaintForm(request.POST)
        if complaint_form.is_valid:
            complaint = complaint_form.save(commit=False)
            student = Student.objects.get(user=request.user)
            complaint.student = student
            complaint.save()
            messages.info(request, 'Complaint Added Successful')
            return redirect(reverse('complaint_view_for_stud', kwargs={'id': request.user.id}))
    return render(request, 'add_complaint.html', {'complaint_form': complaint_form})


def complaint_view_for_stud(request, id):
    complaint = Complaint.objects.filter(student__user=id).order_by('-date')
    return render(request, 'complaint_view_for_stud.html', {'complaint': complaint})

def complaint_delete(request, id):
    data = Complaint.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect(reverse('complaint_view_for_stud', kwargs={'id': request.user.id}))
    else:
        return redirect(reverse('complaint_view_for_stud', kwargs={'id': request.user.id}))
    
def complaint_view_for_staff(request, id):
    complaint = Complaint.objects.filter(staff__user=id).order_by('-date')
    return render(request, 'complaint_view_for_staff.html', {'complaint': complaint})

def resolve_complaint(request, id):
    complaint = Complaint.objects.get(id=id)
    complaint.status = 'resolved'
    complaint.save()
    return redirect(reverse('complaint_view_for_staff', kwargs={'id': request.user.id}))

def leave_view_for_staff(request, id):
    leave = Leave.objects.filter(staff__user=id).order_by('-date')
    return render(request, 'leave_view_for_staff.html', {'leave': leave})

def approve_leave(request, id):
    leave = Leave.objects.get(id=id)
    leave.status = 'approved'
    leave.save()
    return redirect(reverse('leave_view_for_staff', kwargs={'id': request.user.id}))

def reject_leave(request, id):
    leave = Leave.objects.get(id=id)
    leave.status = 'rejected'
    leave.save()
    return redirect(reverse('leave_view_for_staff', kwargs={'id': request.user.id}))



def complaint_view_for_admin(request):
    complaint = Complaint.objects.all().order_by('-date')
    return render(request, 'complaint_view_for_admin.html', {'complaint': complaint})

def resolve_complaint_admin(request, id):
    complaint = Complaint.objects.get(id=id)
    complaint.status = 'resolved'
    complaint.save()
    return redirect('complaint_view_for_admin')

def leave_view_for_admin(request):
    leave = Leave.objects.all().order_by('-date')
    return render(request, 'leave_view_for_admin.html', {'leave': leave})

def approve_leave_admin(request, id):
    leave = Leave.objects.get(id=id)
    leave.status = 'approved'
    leave.save()
    return redirect('leave_view_for_admin')

def reject_leave_admin(request, id):
    leave = Leave.objects.get(id=id)
    leave.status = 'rejected'
    leave.save()
    return redirect('leave_view_for_admin')

def attendance_view_for_staff(request):
    attendance = Attandance.objects.filter(division__staff__user=request.user).order_by('-date')
    return render(request, 'attendance_view_for_staff.html', {'attendance': attendance})
