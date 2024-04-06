from random import randint


# TODO написать функцию, которая выдает трехзначное число
def three_digit_generator() -> int:
    """Функция генерирует трехзначное число состоящее из трех случайных чисел"""
    total_sign = 3
    num_list = [randint(0, 9) for _ in range(total_sign)]
    result = 0
    for i in num_list:
        result = result * 10 + i
    return result
    # return int(''.join(map(str, num_list)))


print(three_digit_generator())

