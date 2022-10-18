# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]
list_prod_of_pairs = []

for i in range(int(len(list)/2)+(len(list)%2)):
    list_prod_of_pairs.append(list[i]*list[-1-i])

# print(round(len(list)/2, 1))
print(list_prod_of_pairs)