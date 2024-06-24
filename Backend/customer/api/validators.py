from datetime import date, timedelta
from validate_docbr import CPF
import re


def validate_name(name):
    return name.isalpha()


def validate_birth_date(birth_date):
    year = timedelta(days=365)
    year_count = 18 * year
    legal_age = date.today() - year_count

    return birth_date < legal_age


def validate_cpf(cpf_number:str):
    cpf = CPF()
    return cpf.validate(cpf_number)


def validate_phone_number(phone_number):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model, phone_number)
    return response