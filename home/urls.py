from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('Ping/', Ping),
    path('PostInputData/', PostInputData),
    path('GetAnswer/', GetAnswer),
    path('Stop/', Stop),
]
