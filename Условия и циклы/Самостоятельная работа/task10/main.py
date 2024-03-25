list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

# TODO завести отдельные счетчики для четных и нечетных чисел
# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных
# TODO вывести каких чисел больше

even_nums_count = 0  # счетчик четных чисел
odd_nums_count = 0  # счетчик нечетных чисел

for number in list_:
    if number % 2:
        odd_nums_count += 1
    else:
        even_nums_count += 1
if odd_nums_count > even_nums_count:
    print("Нечетных чисел больше")
elif odd_nums_count < even_nums_count:
    print("Четных чисел больше")
else:
    print("Четных и нечеттных одинаковое количество")