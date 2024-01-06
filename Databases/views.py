from django.shortcuts import render
from Home.models import pop_datasets

def Databases(request):
    dbs = pop_datasets.objects.all()
    return render(request, 'databases.html', {'dbs': dbs})
