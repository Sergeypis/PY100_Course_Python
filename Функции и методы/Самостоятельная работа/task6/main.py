ALLOW_SYMBOLS = ["0", "1"]  # Допустимые символы


# Проверить, что в строку входят только символы 1 и 0
def check_string(str_):
    # n = 0
    # for symbol in ALLOW_SYMBOLS:
    #     for val in str_:
    #         if val.isdigit() and symbol == val:
    #             n += 1
    # return True if n == len(str_) and str_ else False

    n = 0
    for val in str_:
        if val in ALLOW_SYMBOLS:
            n += 1
    return True if n == len(str_) and str_ else False


print(check_string("1010101010"))
print(check_string("101021231010103"))
print(check_string("asdawqe"))
print(check_string(""))
