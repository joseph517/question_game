from django.urls import path
from .views import *


urlpatterns = [

    path('create/', CreateGameView.as_view(), name='create_game'),
    path('update/<int:pk>/', UpdateGameView.as_view(), name='update_game'),
    path('delete/<int:pk>/', DeleteGameView.as_view(), name='delete_game'),
    path('list/', ListGameView.as_view(), name='list_game'),
    path('ranking/<int:game_id>/', RankingGameView.as_view(), name='game_ranking'),
    path('assign/', AssignGameToUserView.as_view(), name='assign_game'),
      
]