from django.shortcuts import render
from django.http import HttpResponse
from Home.models import pop_datasets, pop_models, feedbacks

def Home(request):
    main_fds = feedbacks.objects.order_by('-feed_rating')[:3]
    dbs = pop_datasets.objects.all()
    mds = pop_models.objects.all()

    return render(request, 'index.html', {'main_fds': main_fds, 'dbs':dbs, 'mds':mds})

