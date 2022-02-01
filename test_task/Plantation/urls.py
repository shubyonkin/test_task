from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("countries/",views.CountryListView.as_view()),
    path("country/", views.CountryCreateView.as_view()),
    path("country/<int:pk>", views.CountryDetailView.as_view()),
    path("plant/", views.PlantCreateView.as_view()),
    path("plant/<int:pk>", views.PlantDetailView.as_view()),
    path("plants/", views.PlantListView.as_view()),
    path("plantations/", views.PlantationListView.as_view()),
    path("plantation/", views.PlantationCreateView.as_view()),
    path("plantation/<int:pk>", views.PlantationDetailView.as_view())
]