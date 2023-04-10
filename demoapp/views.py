from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):
    # emp = Employee(name="tannu",salary="3000",department_id=1)
    # print(emp)
    # emp.save()
    # get_emp = Employee.objects.values_list("salary").filter(name="tannu")
    # print(get_emp)
    # get_emp_id = Employee.objects.values_list("salary").get(name="tannu")
    # print(get_emp_id)
    # get_emp_like = Employee.objects.filter(name__startswith="ra")
    # print(get_emp_like)
    # get_emp_order = Employee.objects.order_by("name")
    # print(get_emp_order)
    # emps = Employee.objects.all()
    # print(emps[:5])
    departments = Department.objects.all()
    context = {'departments': departments}
    if request.method == "GET":
        action = request.GET.get('action')
        if action == "Edit":
            emp_id = request.GET.get('emp_id')
            # print(emp_id,action)
            employee = Employee.objects.filter(employee_id=emp_id)
            # print(query.employee)
            # for emp in employee:
            #     department_id = emp['department']
            # dept_selected = employee.department
            context = {'departments': departments,'employees':employee}
    # print(context)
    return render(request,'home.html',context)



def adduser(request):
    context = {}
    # departments = Department.objects.all()
    # context = {'departments': departments}
    if request.method == "POST":
        if request.POST.get('edit_id') != "":
            name = request.POST.get('name')
            salary = request.POST.get('salary')
            department_id = request.POST.get('department')
            emp_id= request.POST.get('edit_id')
            # print(name,salary,department_id)
            employee = Employee.objects.filter(pk=emp_id).update(name=name,salary=salary,department_id=department_id)
            return JsonResponse({'status':'updated'})
        else:
            name = request.POST.get('name')
            salary = request.POST.get('salary')
            department_id = request.POST.get('department')
            # print(name,salary,department_id)
            employee = Employee(name=name, salary=salary, department_id=department_id)
            employee.save()
            return JsonResponse({'status':'added'})
    else:
        return JsonResponse({'status':0})

def edituser(request):
    if request.method == "GET":
        action = request.GET.get('action')
        if action == "Edit":
            emp_id = request.GET.get('emp_id')
            print(emp_id,action)
            employee = Employee.objects.filter(employee_id=emp_id)
            # for emp in employee:
            #     department_id = emp['department']
            # dept_selected = employee.department
            context = {'employees':employee}
    print(context)
    return render(request,'home.html',context)

def viewusers(request):
    employees = Employee.objects.all()
    # print(employees)
    context = {'employees':employees}
    return render(request,'viewusers.html',context)

def delete_user(request):
    context = {}
    if request.method == "POST" and request.POST.get('action') == "Delete":
        action = request.POST.get('action')
        emp_id = request.POST.get('emp_id')
        print(action,emp_id)
        employee = Employee.objects.get(employee_id = emp_id)
        if employee.delete():
            return JsonResponse({'status':'deleted'})
        else:
            return JsonResponse({'status':0})