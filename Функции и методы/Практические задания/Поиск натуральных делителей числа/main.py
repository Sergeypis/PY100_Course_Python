def get_list_number_divisors(number):
    # TODO Найдите список делителей числа number
    divisors = []
    for num in range(1, number + 1):
        if not number % num:
            divisors.append(num)
    return divisors


print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))
