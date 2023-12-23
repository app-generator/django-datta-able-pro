from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('maps/google-maps/', views.google_maps, name="google_maps"),
]
