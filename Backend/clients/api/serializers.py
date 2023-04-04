from rest_framework import serializers
from ..models import Client
from .validators import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        if not validate_name(data['name']):
            raise serializers.ValidationError(
                {'name':"The 'name' field must be alphanumeric!"}
            )
        
        if not validate_birth_date(data['birth_date']):
            raise serializers.ValidationError(
                {"birth_date" : "You must have 18 years or more"}
            )
        
        if not validate_cpf(data['cpf_number']):
            raise serializers.ValidationError(
                {"cpf_number":"This CPF is not valid! Try again..."}
            )
        
        if not validate_phone_number(data['phone_number']):
            raise serializers.ValidationError(
                {
                "phone_number":
                "The 'phone_number' field must be in the '(##) #####-####' format."
                }
            )
        
        return data