from django.contrib import admin
from django.urls import path
from Home.views import Home
from About.views import About
from Databases.views import Databases
from Models.views import Models

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('databases/', Databases, name='databases'),
    path('models/', Models, name='models')
]
