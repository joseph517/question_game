from django.urls import path
from .views import *


urlpatterns = [

    path('create/', CreateGameService.as_view(), name='create_game'),
    path('update/<int:pk>/', UpdateGameService.as_view(), name='update_game'),
    path('delete/<int:pk>/', DeleteGameService.as_view(), name='delete_game'),
    path('list/', ListGameService.as_view(), name='list_game'),  
      
]