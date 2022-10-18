# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

min = 1
max = 0
for i in range(len(list)):
    if (list[i] - int(list[i])) > max:
        max = (list[i] - int(list[i]))
    if (list[i] - int(list[i])) !=0 and (list[i] - int(list[i])) < min:
        min = (list[i] - int(list[i]))

print(round((max-min), 2))
