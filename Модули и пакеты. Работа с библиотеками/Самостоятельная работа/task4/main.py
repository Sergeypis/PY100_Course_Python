from random import choice
from collections import Counter


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке
side_list = []

for count in counts:
    for _ in range(count):  # TODO подсчитать количество выпаданий орлов и решек
        side_list.append(choice(coin))

    min_coin = min(Counter(side_list).items(), key=lambda side: side[1])
    side_list.clear()

    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат
    list_freq.append(min_coin[1] / (count - min_coin[1]))

print(list_freq)
