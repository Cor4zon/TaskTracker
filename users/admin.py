# users/admin.py

from django.contrib import admin
from users.models import Employee, PersonalData

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonalData)
class PersonalDataAdmin(admin.ModelAdmin):
    pass
