from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'Dave'
    dict_for_view = {'date':date, 'name':name}
    return render(request, 'base.html', dict_for_view)