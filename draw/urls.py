# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check-in/mobile', views.mobile, name='check_in_mobile'),
    path('check-in/web', views.web, name='check_in_web')
]
