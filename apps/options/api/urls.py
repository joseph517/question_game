from django.urls import path
from .views import *


urlpatterns = [

    path('create/', CreateOptionService.as_view(), name='create_option'),
    path('update/<int:pk>/', UpdateOptionService.as_view(), name='update_option'),
    path('delete/<int:pk>/', DeleteOptionService.as_view(), name='delete_option'),
    path('list/', ListOptionService.as_view(), name='list_option'),  
      
]