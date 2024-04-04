# TODO Напишите функцию decimal_to_hex
def decimal_to_hex() -> dict:
    """"Функция преобразовывает десятичные числа в шестнадцатеричные"""

    return {dec_val: hex(dec_val) for dec_val in range(16)}


if __name__ == '__main__':
    dec_to_hex_dict: dict = decimal_to_hex()
    print(dec_to_hex_dict)  # TODO Распечатайте словарь с десятичными и шестнадцатеричными числами
