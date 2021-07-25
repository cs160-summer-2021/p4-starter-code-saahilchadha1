# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check-in/mobile/3', views.mobile_3, name='check_in_mobile_3'),
    path('check-in/mobile/5', views.mobile_5, name='check_in_mobile_5'),
    path('check-in/mobile/7', views.mobile_7, name='check_in_mobile_7'),
    path('check-in/mobile/text', views.mobile_text, name='check_in_mobile_text'),
    path('check-in/web', views.web, name='check_in_web'),
    path('test', views.test)
]
