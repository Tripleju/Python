"""1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
 является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет    """
#1
# a=int(input('Введите число дня недели для определения выходных: '))
# if a==6 or a==7:
#     print('выходной')
# elif a in range(1,5):
#     print('будни')
# else:
#     print('нет такого дня недели')

#2
# a=int(input('Введите число дня недели для определения выходных: '))
# if 5<a<8:
#     print('выходной')
# elif 0<a<6:
#     print('будни')
# else:
#     print('нет такого дня недели') 

"""  2.Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех
 значений предикат. """

""" for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            a=not(x or y or z)
            b=not(x) and not(y) and not(z)
            print(a==b) """


""" 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:  
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3    """

""" x=int(input('введите координаты X: '))
y=int(input('введите координаты Y: '))
if x>0 and y>0:
    print('1 четверть')
elif x<0 and y>0:
    print('2 четверть')
elif x<0 and y<0:
    print('3 четверть')
else:
    print('4 четверть')  """   

""" 4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
 точек в этой четверти (x и y)."""

""" q=int(input('введите номер четверти: '))
if q==1:
    print('x>0 and y>0')
elif q==2:
    print('x<0 and y>0')
elif q==3:
    print('x<0 and y<0')
elif q==4:
    print('x>0 and y<0')
else:
    print('error') """

""" 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 
2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21 """
#1
""" XA=int(input('введите значение координаты Х точки A: '))
YA=int(input('введите координаты Y точки A: '))
XB=int(input('введите координаты X точки B: '))
YB=int(input('введите координаты Y точки B: '))
AB=((XA-XB)**2+(YA-YB)**2)**0.5
print(AB) """

#2
""" XA=int(input('введите значение координаты Х точки A: '))
YA=int(input('введите координаты Y точки A: '))
XB=int(input('введите координаты X точки B: '))
YB=int(input('введите координаты Y точки B: '))
print(f"{((XA-XB)**2+(YA-YB)**2)**0.5:0.4f}") #форматирование берем 4 знака после запятой """
