from django.urls import path
from classroom_manager_app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login_view',views.loginview,name='login_view'),
    path('logout_view',views.logout_view,name='logout_view'),


    ####################### ADMIN ###########################################

    path('admin_home/', views.admin_home, name='admin_home'),
    path('add_standard/', views.add_standard, name='add_standard'),
    path('standard_view/', views.standard_view, name='standard_view'),
    path('standard_delete/<int:id>', views.standard_delete, name='standard_delete'),
    path('add_division/', views.add_divsion, name='add_division'),
    path('division_view/', views.division_view, name='division_view'),
    path('division_delete/<int:id>', views.division_delete, name='division_delete'),

    path('register_staff', views.staff_register, name='register_staff'),
    path('staff_view', views.staff_view, name='staff_view'),
    path('staff_delete/<int:id>', views.staff_delete, name='staff_delete')
    

]