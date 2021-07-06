from django.urls import path
from .views import IndexView, TestView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # IndexView.as_view() -> executando como função
    path('teste/', TestView.as_view(), name='teste'),
]