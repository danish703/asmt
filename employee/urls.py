from django.urls import path
from . import views
urlpatterns = [
    path('dashbaord/',views.dashbaord,name='employee_dashboard'),
    path('create-employee/',views.create_employee,name='create_employee')
]