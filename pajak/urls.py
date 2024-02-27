from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home-view'),
    path('calculate',views.calculate,name='calculate-view')
]