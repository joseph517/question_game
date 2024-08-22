from django.urls import path
from .views import LogoutView
from .views import CreateUserView, ListUsersView, DeleteUserView

urlpatterns = [

    path('create/', CreateUserView.as_view()),
    path('list/', ListUsersView.as_view()),
    path('delete/<int:pk>/', DeleteUserView.as_view()),
    path('logout/', LogoutView.as_view()),

]