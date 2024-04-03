# TODO Напишите функцию decimal_to_hex
def decimal_to_hex() -> dict:
    """"Функция преобразовывает десятичные числа в шестнадцатеричные"""
    return dict(val for val in enumerate(range(1, 16), 1))


if __name__ == '__main__':
    print(decimal_to_hex())  # TODO Распечатайте словарь с десятичными и шестнадцатеричными числами
