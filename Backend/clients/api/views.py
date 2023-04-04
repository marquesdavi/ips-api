from rest_framework import viewsets
from ..models import Client
from .serializers import ClientSerializer
from django.core.mail import send_mail
from decouple import config


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    http_method_names = ['get', 'post', 'patch']

    def perform_create(self, serializer):
        person_email = self.request.data.get('email_address')
        
        if self.action == 'create':
            send_mail(
                'Test title',
                'Test message',
                config('EMAIL_HOST_USER'),
                [f'{person_email}']
            )

        return serializer.save()
