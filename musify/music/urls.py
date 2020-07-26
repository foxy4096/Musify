from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('music/search/', views.search),
    path('music/<int:myid>', views.music),
]
