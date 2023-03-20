'''
Требуется найти в массиве A[1..N] самый близкий по величине 
элемент к заданному числу X. Пользователь в первой строке 
вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

from random import randint
n = int(input("Введите число: "))
A = []
for i in range(n):
    number = randint(0,10)
    A.append(number)
print(A)
num = int(input("введите число X: "))


def nearest_number(x):
    found = A[0]
    for i in range(n):
        if abs(A[i] - num) < abs(found - num):
            found = A[i]
    return found


print(nearest_number(A))
print(f"ближайшее число: {nearest_number(A)}")