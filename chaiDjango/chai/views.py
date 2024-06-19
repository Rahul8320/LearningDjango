from django.shortcuts import render
from .models import ChaiVariety,ChaiStore
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.
def all_chai(request):
    allChais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'allChais': allChais})

def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai': chai})

def chai_stores(request):
    stores = None
    
    if request.method == "POST":
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = ChaiStore.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarietyForm()

    return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form})