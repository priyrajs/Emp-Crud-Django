from django import forms
from .models import Employee

class MyForm(forms.ModelForm):
  class Meta:
    model = Employee
    fields = ["name", "salary","department",]
    labels = {'fullname': "Name", "salary": "Salary","department":"Department"}