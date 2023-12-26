from django.contrib import admin
from .models import Department, UserLogin,OrderForm


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'wikipedia_link']

admin.site.register(Department,DepartmentAdmin)

class UserLoginAdmin(admin.ModelAdmin):
    list_display = ['username','password']

admin.site.register(UserLogin,UserLoginAdmin)

class OrderFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob','age','gender','phone_number','email','address','department','courses']


admin.site.register(OrderForm,OrderFormAdmin)