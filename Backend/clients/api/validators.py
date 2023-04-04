from datetime import date, timedelta
from validate_docbr import CPF


def valid_name(name):
    return name.isalpha()


def valid_birth_date(birth_date):
    year = timedelta(days=365)
    year_count = 18 * year
    legal_age = date.today() - year_count

    return birth_date < legal_age


def validate_cpf(cpf_number:str):
    cpf = CPF()
    return cpf.validate(cpf_number)