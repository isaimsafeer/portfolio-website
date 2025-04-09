from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
     path('services', views.services, name='services'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])