from django.urls import path
from .views import *


urlpatterns = [

    path('create/', CreateOptionView.as_view(), name='create_option'),
    path('update/<int:pk>/', UpdateOptionView.as_view(), name='update_option'),
    path('delete/<int:pk>/', DeleteOptionView.as_view(), name='delete_option'),
    path('list/', ListOptionView.as_view(), name='list_option'),  
      
]