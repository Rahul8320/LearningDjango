from django.shortcuts import render
from .models import ChaiVariety

# Create your views here.
def all_chai(request):
    allChais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'allChais': allChais})