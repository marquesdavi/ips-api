from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(
        max_length=150, 
        blank=False, 
        null=False
    )

    birth_date = models.DateField(
        blank=False
    )

    cpf_number = models.CharField(
        max_length=11, 
        blank=True, 
        null=False, 
        unique=True
    )

    rg_number = models.CharField(
        max_length=9,
        blank=False,
        null=False,
        unique=True
    )

    issuing_entity = models.Charfield(
        max_lenght=30,
        blank=True
    )

    naturalness = models.CharField(
        max_length=110,
        blank=True
    )

    address = models.CharField(
        max_length=220,
        blank=False,
        null=False
    )

    cep_number = models.CharField(
        max_length=9,
        blank=False,
        null=False
    )

    phone_number = models.Charfield(
        max_lenght=14
    )

    email_address = models.EmailField(
        blank=False, 
        max_length=80, 
    )
