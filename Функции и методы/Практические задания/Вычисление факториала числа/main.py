# Функция `factorial`
def factorial(n):
    n_ = 1
    if not n:
        return 1
    for i in range(1, n + 1):
        n_ *= i
    return n_


# TODO Вызовите функцию factorial и распечатайте результат
print(f"Факториал числа 0 равен {factorial(0)}")
print(f"Факториал числа 5 равен {factorial(5)}")
