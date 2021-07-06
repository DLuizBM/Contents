from django.shortcuts import render
from rest_framework import viewsets
from .models import Admins, Employees
from .serializer import AdminsSerializer, EmployeesSerializer
from rest_framework.response import Response


class AdminsViewSet(viewsets.ModelViewSet):
    queryset = Admins.objects.all()
    serializer_class = AdminsSerializer

    def get_queryset(self):
        qs = super(AdminsViewSet, self).get_queryset().filter(name=self.request.user.is_authenticated)  # igual a qs = super().get_queryset()
    #   qs = super(AdminsViewSet, self).get_queryset().exclude(name_id=1)
        return qs


class EmployessViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer





