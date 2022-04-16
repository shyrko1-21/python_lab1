# Найти среднее арифметическое трех последних элементов списка.
import random

list = [random.randint(0,50) for i in range(10)]
sum = 0
for i in range(3):
    sum += list[len(list) - 1 - i]
print(f"Элементы списка: {list}")
print(f"Среднее арифметическое  = {sum / 3.0: .2f}")
