# Функция `is_palindrome`
def is_palindrome(string):
    str_ = "".join(string.lower().split())
    return str_ == str_[::-1]

print("Строка: А роза упала на лапу Азора, является палиндромом: ", is_palindrome("А роза упала на лапу Азора"))
