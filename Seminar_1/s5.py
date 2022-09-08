#2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#*Примеры:*
#- 6,78 -> 7
#- 5 -> нет
#- 0,34 -> 3
#1
""" a=float(input())
b=a*10%10
if b!=0:
    print(int(b))
else:
    print('нет') """

#2
""" a=float(input())
if a%1==0:
    print('no')
else:
    print(int(a*10)%10) """

#3
a=input()
if '.' not in a:
    print('no')
else:
    print(a.index('.')+1) #ищет индекс следующее за знаком точки и выводит этот знак

#4
""" a = input()
if '.' in a:
print(a[a.index('.') + 1])
elif ',' in a:
print(a[a.index(',') + 1])
else:
print('нет') """