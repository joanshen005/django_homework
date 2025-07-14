from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django_filters import rest_framework as filter

class TodoFilter(filter.FilterSet):
    class Meta:
        model = Todo
        fields = ('title',)

class TodoViewSet(viewsets.ModelViewSet):
    # http_method_names = ['get']
    queryset = Todo.objects.all().order_by('-created_time')
    serializer_class = TodoSerializer
    filterset_class = TodoFilter

class CreateModelMixin:
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}