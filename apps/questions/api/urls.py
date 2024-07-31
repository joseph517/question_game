from django.urls import path
from .views import *


urlpatterns = [

    path('create/', CreateQuestionService.as_view(), name='create_question'),
    path('update/<int:pk>/', UpdateQuestionService.as_view(), name='update_question'),
    path('delete/<int:pk>/', DeleteQuestionService.as_view(), name='delete_question'),
    path('list/', ListQuestionService.as_view(), name='list_question'),
    path('validate/', ValidateAnswerView.as_view(), name='validate_answer'), 
       
]