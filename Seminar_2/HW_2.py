""" 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 """
#1 вариант
# num=float(input('введите число: '))
# new_num=int(str(num).replace('.',''))
# sum = 0
# while (new_num != 0):
#     sum = sum + new_num % 10
#     new_num = new_num // 10
# print("Сумма цифр числа равна: ", sum)

#2 вариант
# num=float(input('введите число: '))
# len_num=len(str(num))
# new_num=num*(10**len_num)
# sum = 0
# while (new_num != 0):
#     sum = sum + new_num % 10
#     new_num = new_num // 10
# print("Сумма цифр числа равна: ", int(sum))


""" 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

# N=int(input('введите число: '))
# num=1
# for i in range(1,N):
#     num=num*i
#     print(num,end=', ')
# print(num*(N))

""" 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
Для n = 6: [2, 2, 2, 2, 2, 3] -> 13"""

# n=int(input('введите число: '))
# sum=0
# list=[]
# for i in range(1,n+1):
#     num=round((1+1/i)**i)
#     sum=sum+num
#     list.append(num)
# print(list)
# print(sum)


""" 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите
 произведение элементов на указанных позициях."""

# N=int(input('задайте количество элементов списка: '))
# pos1=int(input('позиция первого элемента: '))
# pos2=int(input('позиция первого элемента: '))
# try:
#     list=[]
#     for i in range(-N,N+1):
#         list.append(i)
#     print(list)
#     print(list[pos1-1]*list[pos2-1])
# except:
#     print('указанные позиции элементов не входят в нужный диапазон')

#5. Реализуйте алгоритм перемешивания списка.
n=int(input('введите число: '))
list=[]

for i in range(n):
    list.append(i)
print(list)
import random
for i in range(n):
    ind1=random.randrange(n)
    ind2=random.randrange(n)
    list[ind1], list[ind2]=list[ind2], list[ind1]
print(list)