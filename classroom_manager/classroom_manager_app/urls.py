from django.urls import path
from classroom_manager_app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login_view',views.loginview,name='login_view'),
    path('logout_view',views.logout_view,name='logout_view'),


    ####################### ADMIN ###########################################

    path('admin_home/', views.admin_home, name='admin_home'),
    path('staff_home/', views.staff_home, name='staff_home'),
    path('add_standard/', views.add_standard, name='add_standard'),
    path('standard_view/', views.standard_view, name='standard_view'),
    path('standard_delete/<int:id>', views.standard_delete, name='standard_delete'),
    path('add_division/', views.add_divsion, name='add_division'),
    path('division_view/', views.division_view, name='division_view'),
    path('division_delete/<int:id>', views.division_delete, name='division_delete'),

    path('register_staff', views.staff_register, name='register_staff'),
    path('staff_view', views.staff_view, name='staff_view'),
    path('staff_delete/<int:id>', views.staff_delete, name='staff_delete'),
    path('standard_view_staff', views.standard_view_staff, name='standard_view_staff'),
    path('division_view_staff', views.division_view_staff, name='division_view_staff'),

    path('staff_view_for_staff', views.staff_view_for_staff, name='staff_view_for_staff'),
    path('student_register', views.student_register, name='student_register'),
    path('student_view', views.student_view_for_staff, name='student_view'),
    path('student_view_admin', views.student_view_for_admin, name='student_view_admin'),
    path('add_attendance', views.add_attendance, name='add_attendance'),
    path('mark_attendance/<int:id>', views.mark_attendance, name='mark_attendance'),
    # path('view_attendance', views.attendance_view_for_staff, name='view_attendance'),

    path('student_home', views.student_home, name='student_home'),
    path('staff_view_for_student', views.staff_view_for_student, name='staff_view_for_student'),
    path('attendance_view_for_student/<int:id>', views.attendance_view_for_student, name='attendance_view_for_student'),
    path('add_leave', views.add_leave, name='add_leave'),
    path('leave_view_for_stud/<int:id>', views.leave_view_for_stud, name='leave_view_for_stud'),
    path('leave_delete/<int:id>', views.leave_delete, name='leave_delete'),

    path('add_complaint', views.add_complaint, name='add_complaint'),
    path('complaint_view_for_stud/<int:id>', views.complaint_view_for_stud, name='complaint_view_for_stud'),
    path('complaint_delete/<int:id>', views.complaint_delete, name='complaint_delete'),

    path('complaint_view_for_staff/<int:id>', views.complaint_view_for_staff, name='complaint_view_for_staff'),
    path('resolve_complaint/<int:id>', views.resolve_complaint, name='resolve_complaint'),

    path('leave_view_for_staff/<int:id>', views.leave_view_for_staff, name='leave_view_for_staff'),
    path('approve_leave/<int:id>/', views.approve_leave, name='approve_leave'),
    path('reject_leave/<int:id>/', views.reject_leave, name='reject_leave'),
    path('attendance_view_for_staff', views.attendance_view_for_staff, name='attendance_view_for_staff'),


    path('complaint_view_for_admin', views.complaint_view_for_admin, name='complaint_view_for_admin'),
    path('resolve_complaint_admin/<int:id>', views.resolve_complaint_admin, name='resolve_complaint_admin'),

    path('leave_view_for_admin', views.leave_view_for_admin, name='leave_view_for_admin'),
    path('approve_leave_admin/<int:id>/', views.approve_leave_admin, name='approve_leave_admin'),
    path('reject_leave_admin/<int:id>/', views.reject_leave_admin, name='reject_leave_admin'),




    

]