"""escola URL Configuration

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

from cursos.urls import router

urlpatterns = [
    # informando ao projeto sobre as rotas na aplicação
    path('api/v1/', include('cursos.urls')),
    # quando alguém digitar api/v1/, manda pra cursos.urls, ou seja, pro arquivo cursos.urls
    # em cursos.urls há 2 opções, cursos e avalicoes, logo deve-se completar
    # api/v1/cursos ou api/v1/avaliacoes
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/v2/', include(router.urls))

]