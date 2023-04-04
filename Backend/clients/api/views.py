from rest_framework import viewsets
from ..models import Client
from .serializers import ClientSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    http_method_names = ['get', 'post', 'patch']