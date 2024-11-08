from django.urls import path
from . import views

urlpatterns = [
    path("lista_juegos/",views.GameList,name="Game list"),
]