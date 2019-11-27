from django.shortcuts import render,redirect
from .forms import EmployeForm,EmployeEditForm,EmployeImageEditForm,ExperineceForm,SkillForm
from .models import Employee,Experience,Skill
# Create your views here.
def dashbaord(request):
    e = Employee.objects.get(user_id=request.user.id)
    x = EmployeEditForm(request.POST or None,instance=e)
    iform = EmployeImageEditForm(request.POST or None,request.FILES or None,instance=e)
    exp = ExperineceForm(request.POST or None)
    experinces = Experience.objects.filter(employee_id = getCurrentlyLogInEmployeeId(request.user.id))
    skillform = SkillForm(request.POST or None)
    skill = Skill.objects.filter(employee_id = getCurrentlyLogInEmployeeId(request.user.id))
    if skillform.is_valid():
        data = skillform.save(commit=False)
        data.employee_id = getCurrentlyLogInEmployeeId(request.user.id)
        data.save()
        return redirect('employee_dashboard')

    if exp.is_valid():
        data = exp.save(commit=False)
        data.employee_id =getCurrentlyLogInEmployeeId(request.user.id)
        data.save()
        return redirect('employee_dashboard')

    if x.is_valid():
        x.save()
        return redirect('employee_dashboard')

    if iform.is_valid():
        iform.save()
        return redirect('employee_dashboard')


    context = {
        'emp':e,
        'eform':x,
        'iform':iform,
        'expform':exp,
        'exp':experinces,
        'skillform':skillform,
        'skill':skill,
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



def exp_edit(request,id):
    exp = Experience.objects.get(pk=id)
    form = ExperineceForm(request.POST or None,instance=exp)
    if form.is_valid():
        form.save()
        return redirect('employee_dashboard')
    context = {
        'form':form
    }
    return render(request,'edit_exp.html',context)

def del_exp(request,id):
    exp = Experience.objects.get(pk=id)
    exp.delete()
    return redirect('employee_dashboard')
