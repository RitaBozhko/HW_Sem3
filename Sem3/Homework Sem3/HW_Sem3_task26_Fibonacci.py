# Задайте число. 
# Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from platform import libc_ver


k = int(input("Введите число: "))
list_Fib_nums_pos = [0, 1]
list_Fib_nums_neg = []


for i in range(2, k+1):
    list_Fib_nums_pos.append(list_Fib_nums_pos[i-1] + list_Fib_nums_pos[i-2])

for i in range (-k, 0):
    list_Fib_nums_neg.append(int((-1)**(i+1)*list_Fib_nums_pos[-i]))
    # print(i, (-i))

print(list_Fib_nums_neg + list_Fib_nums_pos)

