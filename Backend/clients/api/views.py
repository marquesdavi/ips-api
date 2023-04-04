from rest_framework import viewsets
from ..models import Client
from .serializers import ClientSerializer
from django.core.mail import send_mail
from decouple import config
from rest_framework import serializers


class ClientsViewSet(viewsets.ModelViewSet):
    """This viewset consists in create, list and update the clients"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    http_method_names = ['get', 'post', 'patch']

    def perform_create(self, serializer):
        person_email = self.request.data.get('email_address')
        try:
            if self.action == 'create':
                send_mail(
                    'Test title',
                    'Test message',
                    config('EMAIL_HOST_USER'),
                    [f'{person_email}']
                )
        except:
            raise serializers.ValidationError(
                {'email':'Error sending email! Contact the developer'}
            )

        return serializer.save()

