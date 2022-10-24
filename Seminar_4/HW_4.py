
# 1. Вычислить число c заданной точностью d
# Пример:
""" in
Enter a real number: 9
Enter the required accuracy '0.0001': 0.000001
out
9.000000

in
Enter a real number: 8.98785
Enter the required accuracy '0.0001': 0.001
out
8.988 """


# from decimal import Decimal
# my_num=input('Enter a real number: ')
# my_acc=input('Enter the required accuracy ''0.0001'': ')
# def accur(num,d):
#     print(Decimal(num).quantize(Decimal(d)))
# accur(my_num,my_acc)


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
""" in
54
out
[2, 3, 3, 3]

in
9990
out
[2, 3, 3, 3, 5, 37]

in
650
out
[2, 5, 5, 13] """

# my_num=int(input('Enter number: '))
# def simple_prod(num):
#     list_simple=[]
#     for i in range(num - 1, 1, -1):
#         is_simple = 0 
#         if (num % i == 0):
#             for j in range(i - 1, 1, -1):
#                 if (i % j == 0):
#                     is_simple = is_simple + 1
#             if (is_simple == 0): 
#                 list_simple.append(i)
#     print(list_simple)
# simple_prod(my_num)


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.
""" in
7
out
[4, 5, 3, 3, 4, 1, 2]
[5, 1, 2]

in
-1
out
Negative value of the number of numbers!
[]

in
10
out
[4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
[6, 2, 3, 0, 9] """


# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# 5.** Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.