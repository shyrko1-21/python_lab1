# Определить есть ли среди заданных целых чисел A, B, C, D хотя бы одно чётное.
print("Введите числа A, B, C, D")
a = input()
b = input()
c = input()
d = input()
numbers = [a,b,c,d]

for x in numbers:
    if int(x) % 2 == 0:
        print("Найдено четное число")
        break