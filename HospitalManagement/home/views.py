from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from . models import Departments,Doctors
# Create your views here.

def index(request): 
    person = {
        'name':'Vinayak Dev',
        'age': 24,
        'place':'kannur'
    }

    return render(request,'index.html',person)

def about(request):
    return render(request, "about.html")

def booking(request):
    return render(request,"booking.html")

def doctors(request):
    return render(request, "doctors.html")

def contact(request):
    return render(request, "contact.html")

def department(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }
    return render(request, "department.html",dict_dept)