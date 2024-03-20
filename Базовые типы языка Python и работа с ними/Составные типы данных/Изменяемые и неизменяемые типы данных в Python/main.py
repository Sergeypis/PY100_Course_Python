# TODO исправьте опечатку в слове
fruits = ["яблоко", "банан", "опельсин", "виноград"]
orange = fruits[2]
orange = "a" + orange[1:]
fruits[2] = orange
print(fruits)
