from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Department(models.Model):
    department_id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    name = models.CharField(max_length=100)
    salary = models.CharField(max_length=50,null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,default=1,related_name='id')

    def __str__(self):
        return self.name

