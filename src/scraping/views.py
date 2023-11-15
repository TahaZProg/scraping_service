from django.shortcuts import render
from .models import Vacansy

def home_view(request):
    qs = Vacansy.objects.all()
    return render(request, 'scraping/home.html', {'object_list' : qs})
