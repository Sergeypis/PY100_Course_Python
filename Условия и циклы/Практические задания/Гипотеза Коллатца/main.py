num = 27  # Число для проверки гипотезы Коллатца
count = 0  # Количество операций над числом

# TODO Посчитайте количество действий над числом по гипотезе Коллатца
while True:
    if not num % 2:
        num = num // 2
    elif num % 2:
        num = num * 3 + 1
    count += 1
    if num == 1:
        break
print("Количество действий:", count)
