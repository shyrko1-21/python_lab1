# 2. Торговая фирма в первый день работы реализовала товаров на P тыс. руб., а затем ежедневно увеличивала
# выручку на 3%. Какой будет выручка фирмы в тот день, когда она впервые превысит заданное значение Q? Сколько
# дней придется торговать фирме для достижения этого результата?

print("Введите P")
p = int(input())
print("Введите Q")
q = int(input())

i = 1
while True:
    p *= 1.03
    i += 1
    if p > q:
        break
print(f"Выручка равна {p}, количество дней равно {i}")
