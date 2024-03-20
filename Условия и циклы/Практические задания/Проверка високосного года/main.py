year = 2012

if (not year % 4) and (year % 100 or not year % 400):  # TODO Напишите условие проверки високосного года
    print(year, "является високосным годом.")
else:
    print(year, "не является високосным годом.")
