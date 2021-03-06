# Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99). Размер списка n ввести с клавиатуры. В соответствии со своим вариантом написать программу по условию, представленному в таблице ниже.
# Найти среднее арифметическое трех последних элементов списка.

import random

print("Введите размер списка")
n = int(input())

A = [random.randint(0, 99) for i in range(n)]

print(f"Исходный список: {A}")
print(f"Среднее арифметическое трех последних элементов: {(A[-1] + A[-2] + A[-3]) / 3}")