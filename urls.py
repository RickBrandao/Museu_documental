from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('documentos/', views.documentos, name='documentos'),
    path('sobre/', views.sobre, name='sobre'),
    path('documentos/paroquia-neves/', views.paroquia_neves, name='paroquia_neves'),
]
