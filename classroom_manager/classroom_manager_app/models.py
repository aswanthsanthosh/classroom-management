from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if email:
            email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, email, password, **extra_fields)


USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('student', 'student'),
    )

class CustomUser(AbstractUser):
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES
    )

    objects = CustomUserManager()
    

    # def is_admin(self):
    #     return self.user_type == 'admin'

    # def is_staff(self):
    #     return self.user_type == 'staff'

    # def is_student(self):
    #     return self.user_type == 'student'
    
class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='adminuser',null=True,blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return self.email

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='staffuser',null=True,blank=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='student',null=True,blank=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=12, null=True, blank=True)
    parent_contact = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    division = models.ForeignKey('Division', 
                                 on_delete=models.CASCADE,
                                 related_name='student')
    
    def __str__(self) -> str:
        return self.name

class Standard(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Division(models.Model):
    division = models.CharField(max_length=100)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='division')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='divisions')

    def __str__(self) -> str:
        return self.division

ATTENDANCE_STATUS_CHOICES = (('present', 'present'),
                             ('absent', 'absent'))

class Attandance(models.Model):
    date = models.DateField()
    status = models.CharField(choices=ATTENDANCE_STATUS_CHOICES,
                              max_length=20,
                              default='present')
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='attendance'
    )
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE,
        related_name='attendance'
    )


LEAVE_STATUS_CHOICES = (('approved', 'approved'),
                        ('rejected', 'rejected'),
                        ('pending', 'pending'),)

class Leave(models.Model):
    date = models.DateField()
    reason = models.TextField()
    status = models.CharField(
        choices=LEAVE_STATUS_CHOICES,
        default='pending', max_length=10
    )
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE,
        related_name='leave'
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='leave'
    )
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE,
        related_name='leave',
        null=True, blank=True
    )


COMPLAINT_STATUS = (('open', 'open'),
                    ('resolved', 'resolved'))

class Complaint(models.Model):
    complaint_text = models.TextField()
    status = models.CharField(
        choices=COMPLAINT_STATUS,
        default='open', max_length=10
    )
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE,
        related_name='complaint'
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='complaint'
    )
    staff = models.ForeignKey(Staff, 
                              on_delete=models.CASCADE, 
                              related_name='complaint')
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    