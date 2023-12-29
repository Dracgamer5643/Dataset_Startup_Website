from django.contrib import admin
from Home.models import pop_datasets, pop_models

# Register your models here.
admin.site.register(pop_models)
admin.site.register(pop_datasets)
