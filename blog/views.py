from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee

# Create your views here.

def index(request):
    return HttpResponse("This is my first url")

def specific(request):
    list1 = [1, 2, 3, 4]
    return HttpResponse(list1)

# def article(request, article_id):
#     return render(request, 'blog/index.html', {'article_id': article_id})
def showEmployeeForm(request):
    return render(request, 'blog/employeeForm.html')

def createEmployee(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        job = request.POST.get('job')
        salary = request.POST.get('salary')
        employee = Employee()
        employee.name = name
        employee.email = email
        employee.job = job
        employee.salary = salary
        employee.save()
        return redirect('index')
    return redirect('index')
