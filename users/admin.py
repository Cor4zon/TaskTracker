from django.contrib import admin

from users.models import Employee, PersonalData
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonalData)
class PersonalDataAdmin(admin.ModelAdmin):
    pass
