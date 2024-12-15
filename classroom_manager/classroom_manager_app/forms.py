from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Standard, Division, Staff, Complaint, Leave, Student, Attandance



class LoginForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class StandardForm(forms.ModelForm):
    class Meta:
        model = Standard
        fields = "__all__"

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = "__all__"

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"
        exclude = ['user']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ['user']

class CompalaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = "__all__"
        exclude = ['status', 'student']

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = "__all__"
        exclude = ['student', 'status', 'division']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attandance
        fields = "__all__"