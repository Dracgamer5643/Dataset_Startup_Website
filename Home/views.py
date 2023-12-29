from django.shortcuts import render
from django.http import HttpResponse
from Home.models import pop_datasets, pop_models

def Home(request):
    range = 3
    dbs = pop_datasets.objects.all()
    mds = pop_models.objects.all()
    return render(request, 'index.html', {'dbs':dbs, 'range': range, 'mds':mds})

