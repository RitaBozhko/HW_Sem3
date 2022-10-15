# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Ведите число: "))
list = [i for i in range(-n, n+1)]
print(list)

path = 'file.txt'
data = open(path, 'r')

prod = 1
for line in data:
    prod *= list[int(line)]
data.close()

print(prod)