# Реализуйте алгоритм перемешивания списка.

from random import randint


list = [randint(1,20) for i in range(15)]
print(list)

for j in range(len(list)-1):
    for i in range(len(list)-1-j):
        if list[i] > list [i+1]:
            list[i], list[i+1] = list[i+1], list[i]

print(list)
