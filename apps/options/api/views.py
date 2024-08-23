from urllib import response
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.options.api.serializers import OptionSerializer
from apps.options.models import Option
from apps.questions.models import Question
from rest_framework.response import Response



class CreateOptionView(generics.CreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class UpdateOptionView(generics.UpdateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put (self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class DeleteOptionView(generics.DestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_destroy(self, instance):
        instance.delete()

class ListOptionView(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticated]