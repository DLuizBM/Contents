from django.urls import path
from .views import CarroView, ToyotaView, HondaView

urlpatterns = [
    path('', CarroView.as_view(), name='index'),
    path('Toyota/<int:pk>', ToyotaView.as_view(), name='Toyota'),
    path('honda/<int:pk>', HondaView.as_view(), name='honda'),
]
