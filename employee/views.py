from django.shortcuts import render,redirect
from .forms import EmployeForm,EmployeEditForm,EmployeImageEditForm
from .models import Employee
# Create your views here.
def dashbaord(request):
    e = Employee.objects.get(user_id=request.user.id)
    x = EmployeEditForm(request.POST or None,instance=e)
    iform = EmployeImageEditForm(request.POST or None,request.FILES or None,instance=e)
    if x.is_valid():
        x.save()
        return redirect('employee_dashboard')

    if iform.is_valid():
        iform.save()
        return redirect('employee_dashboard')

    context = {
        'emp':e,
        'eform':x,
        'iform':iform
    }
    return render(request,'employee_dashboard.html',context)

def create_employee(request):
    if request.method=='GET':
        context = {
            'form':EmployeForm()
        }
        return render(request,'create_employee.html',context)
    else:
        form = EmployeForm(request.POST,request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('employee_dashboard')
        else:
            return render(request,'create_employee.html',{'form':form})

def getCurrentlyLogInEmployeeId(id):
    e = Employee.objects.get(user_id=id)
    return e.id

