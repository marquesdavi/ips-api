from django.db import models

# Create your models here.

class Customer(models.Model):
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

    issuing_entity = models.CharField(
        max_length=30,
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

    phone_number = models.CharField(
        max_length=14,
        blank=True
    )

    email_address = models.EmailField(
        blank=True, 
        max_length=80, 
    )
