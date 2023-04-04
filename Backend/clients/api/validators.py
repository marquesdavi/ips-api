from datetime import date, timedelta


def valid_name(name):
    return name.isalpha()


def valid_birth_date(birth_date):
    year = timedelta(days=365)
    year_count = 18 * year
    legal_age = date.today() - year_count

    return birth_date < legal_age


