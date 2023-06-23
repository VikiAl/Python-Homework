# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# N = int(input('N = '))
# nums = []
# for i in range(N):
#     nums.insert(i, int(input()))
#     i+=1
# print(nums)
# x= int(input('x= '))
# k=0
# for j in range(len(nums)):
#     if nums[j] == x:
#         k+=1
# print('x встречается',k, 'раз')

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# N = int(input('N = '))
# nums = []
# for i in range(N):
#     nums.insert(i, int(input()))
#     i+=1
# print(nums)
# x= int(input('x= '))
# min=2147483647   # как присвоить min максимальное возможное значение?
# k=x
# for i in range(len(nums)):
#     if nums[i]>x:
#         if nums[i]-x <min:
#             k=nums[i]
#             min=nums[i]-x
#     else:
#         if x-nums[i]<min:
#             k=nums[i]
#             min=x-nums[i]

# print(k)

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, 
# что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
# 12    

scrabble = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1,'L':1, 'N':1, 'S':1, 'T':1, 'R': 1, 
            'D':2, 'G':2, 
            'B':3, 'C':3, 'M':3, 'P':3, 
            'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 
            'K':5, 
            'J':8, 'X':8, 
            'Q,':10, 'Z':10,
            'А':1, 'В':1, 'Е':1,'И':1,'Н':1,'О':1,'Р':1,'С':1,'Т':1,
            'Д':2,'К':2,'Л':2,'М':2,'П':2,'У':2,
            'Б':3,'Г':3,'Ё':3,'Ь':3,'Я':3,
            'Й':4,'Ы':4,
            'Ж':5,'З':5,'Х':5,'Ц':5,'Ч':5,
            'Ш':8,'Э':8,'Ю':8,
            'Ф':10,'Щ':10,'Ъ':10,
            }
sum=0
x= str(input ('Введите слово: ')).upper()

for i in x:
    if i in scrabble:
        sum = sum+scrabble[i]
print('количество очков: ',sum)