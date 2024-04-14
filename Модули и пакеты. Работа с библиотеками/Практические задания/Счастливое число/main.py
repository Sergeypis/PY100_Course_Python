def is_lucky_number(num: int) -> bool:
    len_num = len(str(num))
    if isinstance(num, int):  # TODO проверить что число шестизначное и положительное
        if num > 0 and len_num == 6:
            sum_left = sum([int(i) for i in str(num)[:len_num // 2]])
            sum_right = sum([int(i) for i in str(num)[len_num // 2:]])
        else:
            raise ValueError("Число не является шестизначным или положительным")
    else:
        raise TypeError(f"Тип {type(num)} не является int")

    return sum_left == sum_right  # TODO проверить счастливое число или нет


print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
