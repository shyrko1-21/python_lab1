# Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99). Размер списка n ввести с клавиатуры. В соответствии со своим вариантом написать программу по условию, представленному в таблице ниже.
# Удалить элементы, индексы которых кратны 3.

import random

print("Введите размер списка")
n = int(input())

A = [random.randint(0, 99) for i in range(n)]
print(f"Исходный список: {A}")

index = 1
delta = 0
initLen = len(A)
for i in range(initLen):
    if index % 3 == 0:
        A.remove(A[index - delta])
        delta += 1
    index += 1

print(f"Список после удаления: {A}")


