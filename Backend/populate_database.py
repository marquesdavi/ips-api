import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from clients.models import Client

def populate(n):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(n):
        cpf_number = CPF()
        name = fake.name()
        birth_date = '{}-{}-{}'.format(random.randrange(1960, 2003), random.randrange(10, 12), random.randrange(1, 30))
        email_address = '{}@{}'.format(name.lower(),fake.free_email_domain())
        email_address = email_address.replace(' ', '')
        cpf_number = cpf_number.generate()
        rg_number = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
        phone_number = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        address = fake.address()
        cep_number = "{}{}-{}".format(random.randrange(10, 21), random.randrange(100, 210), random.randrange(100, 210))
        p = Client(
            name=name, 
            birth_date=birth_date,
            email_address=email_address, 
            cpf_number=cpf_number, 
            rg_number=rg_number, 
            phone_number=phone_number, 
            naturalness="Brazilian",
            address=address,
            cep_number=cep_number
            )
        p.save()
        
    print(f'{n} people created succesfully!')

populate(50)
