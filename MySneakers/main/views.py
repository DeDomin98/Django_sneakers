from django.shortcuts import render
from django.http import request
# Create your views here.
from .models import Sneakers

def home(request):

    sneakers = Sneakers.objects.all()

    
    total_value = 0
    try:
        for item in sneakers:
            total_value += item.price
    except:
        pass

    context = {
    'sneakers': sneakers, 
    'sneakers_count': len(sneakers),
    'total_value': total_value
    }
    
    return render (request, 'main/home.html', context)
    
    
    
def start(request):
    return render (request, 'main/start.html', {})
