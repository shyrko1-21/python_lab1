# Удалить элементы, индексы которых кратны 3.

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(f"Элементы начального списка: {list}")
listToDel = []

for i in range(3, len(list)):
    if i % 3 == 0:
        listToDel.append(list[i])

for i in range(len(listToDel)):
    list.remove(listToDel[i])

print(f"Элементы списка после удаления: {list}")


