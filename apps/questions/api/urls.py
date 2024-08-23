from django.urls import path
from .views import *


urlpatterns = [

    path('create/', CreateQuestionView.as_view(), name='create_question'),
    # path('update/<int:pk>/', UpdateQuestionView.as_view(), name='update_question'),
    path('delete/<int:pk>/', DeleteQuestionView.as_view(), name='delete_question'),
    path('list/', ListQuestionView.as_view(), name='list_question'),
    path('list/<int:game_id>/', ListQuestionByGame.as_view(), name='list_question'),
    path('validate/', ValidateAnswerView.as_view(), name='validate_answer'), 
       
]