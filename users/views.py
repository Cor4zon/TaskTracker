# users/views.py
from django.shortcuts import render
from users.models import Employee, PersonalData

# Create your views here.
def index(request):
    return render(request, "base.html")


def all_employees(request):
    employees = Employee.objects.all()
    return render(request, "all_employees.html", context={"employees": employees})


def personal_data(request, pk):
    employee_id = Employee.objects.get(pk=pk).id
    print("id: ", employee_id)
    personal_data = PersonalData.objects.get(employee_id=employee_id)
    return render(request, "personal_data.html", context={"personal_data": personal_data})



