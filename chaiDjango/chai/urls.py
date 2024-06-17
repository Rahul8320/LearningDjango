from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.all_chai, name='all_chai'),
]
