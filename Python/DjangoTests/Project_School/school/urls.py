"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

# Configuração sem endpoint, para cada view, na tela inicial da API
# from rest_framework.routers import SimpleRouter
# router = SimplesRouter()
# router.register('adms', AdminsViewSet)

# Configuração com endpoints, para cada view, na tela inicial da API (API root)
from core import views
from core.views import AdminsViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('adms', views.AdminsViewSet)
router.register('employees', views.EmployessViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
