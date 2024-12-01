from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Standard, Division, Staff, Complaint, Leave



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

class CompalaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = "__all__"

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = "__all__"