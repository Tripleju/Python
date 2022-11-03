print('hello world')

# типы данных и переменные
a= 1
b=1.23
value=None
value=1234
s='Hello "world'
#print(type(b))
#print(type(value))

#print(s) #вывод строки
#print(a,'-',b,'-',s)
#print('{} - {} - {}'.format(a,b,s))
#print(f'{a} - {b} - {s}')
#print('{1} - {2} - {0}'.format(a,b,s))
f=False

#ввод и вывод данных
#list=[1,2,3]
#print(list)

print('введите a')
a=int(input())
print('введите b')
b=int(input())
print(a, '+', b, '=', a+b)
print('{} {}'.format(a,b))

#Арифметические операции
a=14
b=5
c= a//b #целочисленное деление
c= a%b # остаток от деления
c= a**b #возведение в степень

# Логические операции
a=1<4
print(a)
b=1==2
c=1<3<5<10

func=1
T=1
x=123
print(func<T>(x))

f=[1,2,3,4]
print(not 2 in f)

is_odd=f[0]%2==0
print(is_odd)

is_odd=not f[0]%2

#управляющие конструкции
a=int(input('a='))
b=int(input('b='))
if a>b:
    print(a)
else:
    print(b)


username=input('Введите имя: ')
if username=='Маша':
    print('Ура, это же МАША!')
elif username=='Марина':
    print('Ильнар - топ')
else:
    print('Привет, ', username)


original=23
inverted=0
while original !=0:
    inverted=inverted*10+(original%10)
    original//=10
print(inverted)

# while-else

original=23
inverted=0
while original !=0:
    inverted=inverted*10+(original%10)
    original//=10
else:
    print('Пожалуй')
    print('хватит')
print(inverted)

# for

for i in 1,2,3,4,5:
    print(i**2)

list=[1,2,3,4,5]
for i in list:
    print(i)
