#2. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#*Пример:*
#- [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19
from random import uniform
n=int(input("Введите размер списка: "))
list=[]
for i in range(n):
    f=uniform(0,9)
    list.append(round(f, 2))

min=list[0]
max=0
for i in range(len(list)):
    if max<list[i]:
        max=list[i]
    if min>list[i]:
        min=list[i]
dif = (max - int(max)) - (min - int(min))
print(list)
print(max,min)
print(round(dif,2))





