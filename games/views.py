from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse
from .models import Games
from django.template import loader
# Create your views here.


def GameList(request):
    if request.method == "GET":
        games = Games.objects.all()
        template = loader.get_template("games/index.html")
        datos = {"game_list":games}
        return HttpResponse(template.render(datos,request))
    else:
        return HttpResponse("Metodo no valido")















# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializer import GamesSerializer
# class GameList(APIView):
#     def get(self,request):
#         games = Games.objects.all()
#         serializer = GamesSerializer(games, many=True)
#         if serializer.data == []:
#             return Response("No hay juegos que mostrar")
#         else:
#             return Response(serializer.data)
    