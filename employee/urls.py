from django.urls import path
from . import views
urlpatterns = [
    path('dashbaord/',views.dashbaord,name='employee_dashboard'),
    path('create-employee/',views.create_employee,name='create_employee'),
    path('experience/edit/<int:id>',views.exp_edit,name='exp_edit'),
    path('experience/delete/<int:id>',views.del_exp,name='exp_del'),
]