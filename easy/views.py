from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from company.models import Company
from employee.models import Employee



def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        u = request.POST.get('username')
        p1 = request.POST.get('pass1')
        p2 = request.POST.get('pass2')
        if p1==p2:
            user = User(username = u)
            user.set_password(p1)
            user.save()
            messages.add_message(request,messages.SUCCESS,'your account is created')
            return redirect('login')
        else:
            messages.add_message(request,messages.ERROR,'Password does not match')
            return redirect('signup')


def signin(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        u = request.POST.get('username')
        p = request.POST.get('pass1')
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            w = whoareyou(request.user.id)
            if w==1:
                return redirect('employee_dashboard')
            elif w==2:
                return redirect('company_dashboard')
            else:
                return redirect('who')

        else:
            messages.add_message(request,messages.ERROR,'username or password does not match')
            return redirect('login')


def signout(request):
    logout(request)
    return redirect('login')

def who(request):
    return render(request, 'who.html')




def whoareyou(id):
    try:
        a= Employee.objects.get(user_id=id)
        return 1
    except:
        try:
            c = Company.objects.get(user_id=id)
            return 2
        except:
            return 0








