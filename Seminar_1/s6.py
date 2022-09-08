#3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
#1
""" a=int(input('введите число: '))
if a%30==0:
    print('no')
elif (a%10==0 or a%15==0) and a%5==0:
    print('yes')
else:
    print('no') """

#2
n=int(input())
if (n%5==0 and n%10==0 or n%15==0) and n%30!=0:
    print(True)
else:
    print(False)

