# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:
# 6782 -> 23
# 0,56 -> 11

n = input("Ведите число: ")

num_of_digits = len(n)
n = int(float(n) * 10**(num_of_digits))
print(num_of_digits, n)

sum = 0
while n > 0:
    sum+=n%10
    n=n//10
print(int(sum))

# float_num = input("Введите вещественное число: ")
# sum = 0
# for i in float_num:
#     if i != ",":
#         sum += int(i)
# print(sum)
