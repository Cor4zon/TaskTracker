from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)


class PersonalData(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=30)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    photo = models.FilePathField(path="", blank=True)
