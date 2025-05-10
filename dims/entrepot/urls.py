from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
path('entrepots/', views.entrepot_listing, name='entrepot-listing'),
path('new/', views.create_entrepot, name='entrepot-create'),
]