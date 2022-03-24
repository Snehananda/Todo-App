from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('create/', views.create, name="create"),
    path('display/', views.displayEvents, name="display"),
    path('update/', views.update, name="update"),
    path('delete/', views.delete, name="delete"),
    path('create-event/', views.createEvent),
    path('update-event/', views.updateEvent),
    path('delete-event/', views.deleteEvent)
]
