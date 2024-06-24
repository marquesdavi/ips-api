from rest_framework import viewsets
from ..models import Customer
from .serializers import ClientSerializer
from django.core.mail import send_mail
from decouple import config
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated


class ClientsViewSet(viewsets.ModelViewSet):
    """
    This viewset consists in create, list and update the customer
    """
    queryset = Customer.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated,]

    http_method_names = ['get', 'post', 'patch']

    def perform_create(self, serializer):
        person_email = self.request.data.get('email_address')
        client_name = self.request.data.get('name')
        monthly_fee:int = 100
        service:str = 'service'

        try:
            if self.action == 'create':
                send_mail(
                    f'Confirmação de cadastro - {client_name}',
                    f"""
                    Seu cadastro foi realizado com sucesso!\n
                    Serviço: {service}\n
                    Cliente: {client_name}\n
                    Valor: R$ {float(monthly_fee)}\n
                    """,
                    config('EMAIL_HOST_USER'),
                    [f'{person_email}']
                )
        except:
            raise serializers.ValidationError(
                {'email':'Error sending email! Contact the developer'}
            )

        return serializer.save()

