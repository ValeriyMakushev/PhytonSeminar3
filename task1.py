#1.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  *Пример:*
#   - [2, 3, 4, 5, 6] => [12, 15, 16];
#   - [2, 3, 5, 6] => [12, 15]
import random
list=[2,3,4,5,6]
res=[]
for i in range(len(list)//2):
    res.append(list[i]*list[-i-1])
    if len(list)% 2 != 0:
        m=len(list)//2
        res.append(list[m]*list[m])
        print(list[-i+3])

print(res)



