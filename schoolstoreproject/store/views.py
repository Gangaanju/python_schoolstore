from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Department,UserLogin,OrderForm



def home(request):
    departments = Department.objects.all()
    return render(request, 'home.html', {'departments': departments})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('store:new_page')
        else:
            if User.objects.filter(username=username).exists():
                return render(request,'login.html',{'message': "Incorrect Password"})
            else:
                return render(request,'login.html',{'message': "Username is Invalid"})


    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'message': "Username already exists"})
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                UserLogin.objects.create(username=username,password=password)
                messages.success(request,"User registered successfully")
        else:
                return render(request, 'register.html', {'message': "Password do not match"})
        return redirect('store:login')
    return render(request, 'register.html')



def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('countryCode') + request.POST.get('phoneNumber')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')

        # user, created = User.objects.get_or_create(username=name,email=email)
        user = User.objects.create_user(name=name,email=email)

        user.save()
        OrderForm.objects.create(user=user, name=name, dob=dob, age=age, gender=gender,
                                             phone_number=phone_number, address=address, department=department,
                                             course=course)

        return redirect('store:home')
    return render(request, 'form.html')


def new_page(request):

    return render(request, 'new_page.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def submit_form(request):
    if request.method == 'POST':

        confirmation_message = 'Order Confirmed'


        return render(request, 'submit_form.html', {'confirmation_message': confirmation_message})
    else:
        return render(request, 'form.html')

