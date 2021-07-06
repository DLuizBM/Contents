from django.contrib import admin
from .models import Admins, Employees


@admin.register(Admins)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'id_number')
