from django.shortcuts import render, redirect
from .models import Patient, Contact
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def patient(request):
    return render(request, 'patient.html')

def donor(request):
    return render(request, 'donor.html')

def contact(request):
    if request.method=="POST":
        if request.POST['name']is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            dict={'out':1,'name':request.POST['name']}
            return render(request,'contact.html',dict)
    return render(request,'contact.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            check_user = Patient.objects.get(email = email,password = password)
            request.session['email'] = check_user.email
            request.session['name'] = check_user.name
            request.session['phno'] = check_user.phno
            return redirect('newhome')
        except Patient.DoesNotExist:
            messages.error(request,'invalid username or password')
            return redirect('login')
    return render(request,'.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phno = request.POST['phno']
        address=request.POST['address']
        bdgp=request.POST['bdgp']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if Patient.objects.filter(email = email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                customer = Patient.objects.create(email = email,name = name,password = password,phno = phno,bdgp = bdgp,address = address)
                customer.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password is not match')
            return redirect('register')
    else:
        return render(request,'patient.html')

def forgot(request):
    return render(request, 'forgot.html')

