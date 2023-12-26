from django.contrib.auth.models import User
from django.db import models




class Department(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_link = models.URLField()

    def __str__(self):
        return self.name

class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    def __str__(self):
        return self.username


class OrderForm(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=[('male','Male'),('female','Female'),('other','Other')])
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.CharField(max_length=100)

    # Other fields related to the order

    def __str__(self):
        return self.username




