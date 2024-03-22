# TODO Распечатать таблицу умножения
size = 9
for x in range(2, size + 1):
    for y in range(2, size + 1):
        space = '' if y == size else ' '
        print(f"{x * y:>2}", end=space)
    print()