#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#Примеры:
#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90
#1
""" numbers=[]
n=int(input('введите количество числ: '))

for i in range(n):
    a=int(input('введите число: '))
    numbers.append(a)
maxx=numbers[0]
for i in numbers:
    if i>maxx:
        maxx=i
print(maxx)
 """

#2
""" numbers=[]
n=int(input('введите количество числ: '))

for i in range(n):
    a=int(input('введите число: '))
    numbers.append(a)
print(max(numbers)) """

#3
n=int(input('введите количество числ: '))
maxx=int(input('введите число: '))
for i in range(n-1):
    a=int(input('введите число: '))
    if a>maxx:
        maxx=a
print(maxx)