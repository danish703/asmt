from django.shortcuts import render

# Create your views here.
def dashbaord(request):
    return render(request,'company_dashboard.html')