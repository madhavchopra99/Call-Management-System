from django.urls import path
from . import views

urlpatterns = [
    path('', views.logs, name='logs'),
    path('ivr_histogram/', views.ivr_histogram, name='ivr_histogram'),
    path('result/', views.result, name='result')

]
