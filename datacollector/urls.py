from django.contrib import admin
from django.urls import path
from Home.views import Home
from About.views import About
from Databases.views import Databases
from Models.views import Models
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('databases/', Databases, name='databases'),
    path('models/', Models, name='models')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)