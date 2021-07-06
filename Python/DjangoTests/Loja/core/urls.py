from django.urls import path
from .views import IndexView, ToyotaView, HondaView, VolksView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('toyota/<int:pk>', ToyotaView.as_view(), name='toyota'),
    path('honda/<int:pk>', HondaView.as_view(), name='honda'),
    path('volkswagen/<int:pk>', VolksView.as_view(), name='volkswagen'),
]

