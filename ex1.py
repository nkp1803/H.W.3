'''
Задача 16: Требуется вычислить, сколько раз встречается 
некоторое число X в массиве A[1..N]. Пользователь в первой 
строке вводит натуральное число N – количество элементов в 
массиве. В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    3
    -> 1
'''

#n = int(input("введите размер массива: "))
#numbers = []
#for i in range(n):
#     a = int(input("введите число: "))
#     numbers.append(a)
#print(numbers)
#num = int(input("введите ваше число: "))
#print(f"ваше число повторяется {numbers.count(num)} раз")


from random import randint
n = int(input("введите число: "))
numbers = []
for i in range(n):
     a = randint(0,10)
     numbers.append(a)
print(numbers)
num = int(input("введите число X: "))
print(f" Число X повторяется : {numbers.count(num)} раз")