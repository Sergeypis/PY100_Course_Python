import string
from random import sample


def get_random_password(n: int = 8) -> str:
    """Функция генератор паролей из случайных символов заданной длины - n"""
    list_symbols = sample(string.digits + string.ascii_lowercase + string.ascii_uppercase, n)

    return ''.join(list_symbols)


print(get_random_password())
