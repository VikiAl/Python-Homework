# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# a=int(input('a= '))
# b=int(input('b= '))

# def pw(a,b):
#     if b==1:
#         return a
#     return a*pw(a,b-1)
# print(pw(a,b))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def sum(a,b):
    if b==0:
        return a
    return sum(a,b-1)+1
a=int(input('a= '))
if a<0:
    print('неверное значение a')
b=int(input('b= '))
if b<0:
    print('неверное значение b')
print('сумма =' ,sum(a,b))


    