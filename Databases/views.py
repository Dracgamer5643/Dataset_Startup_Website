from django.shortcuts import render
from Home.models import pop_datasets
from django.core.paginator import Paginator

def Databases(request):
    dbs = pop_datasets.objects.order_by('-db_rating')[:9]
    
    items_per_page = 9
    paginator = Paginator(dbs, items_per_page)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'databases.html', {'dbs': dbs, 'page_obj': page_obj})

