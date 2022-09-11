""" 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
*Пример:*
- Для N = 5: 1, -3, 9, -27, 81

 """
#1
""" n=int(input('введите число: '))
a=-3
for i in range(n-1):
    print(a**i, end=',')
print(a**(n-1))
 """
#2
""" N=int(input())
a=[]
for i in range(N):
    a.append(str(((-3)**i)))
print(', '.join(a)) """

#3
N=int(input())
a=[]
for i in range(N):
    a.append((-3)**i)
print(*a, sep=', ') 
