from django.shortcuts import render

from .forms import FindForm
from .models import Vacansy

def home_view(request):
    #print(request.GET)
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        _filer = {}
        if city:
            _filer['city__slug'] = city
        if language:
            _filer['language__slug'] = language
        qs = Vacansy.objects.filter(**_filer)
    else:
        qs = Vacansy.objects.all()
    return render(request, 'scraping/home.html', {'object_list' : qs, 'form' : form})
