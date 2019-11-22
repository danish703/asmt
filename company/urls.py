from django.urls import path
from . import views
urlpatterns = [
    path('dashbaord/',views.dashbaord,name='company_dashboard')
]