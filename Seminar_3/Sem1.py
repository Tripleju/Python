#1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

""" import time
rand = time.time()
rand = rand * 1000 % 1000
rand = int(rand)
print(rand) """

""" import time
now=time.time(
print(int(str(now).split('.')[1])%100))
 """
#2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
#1
""" lilist_0 = ["qwe", "asd", "zxc", "7qwe", "ertqwe"]
number = input('Enter number: ')
booll = False
for item in list_0:
    if number in item:
        print('Yes')
        booll = True
        break
if booll == False:
    print('No')
 """
#2
""" some_list=[input('введите строку: ') for _ in range(int(input('ввкдите количество элементов')))]
el=input('введите искомое число: ')
for i in some_list:
    if el in i:
        print('yes')
        break
else:
    print('no') """


#size=int(input('enter size'))

#3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

#*Пример:*

""" - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1 """
#1
""" list_0 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
el = "qwe"
count = 0
booll = False
for i in range(len(list_0)):
    if el == list_0[i]:
        count += 1
        if count == 2:
            booll = True
            print(i)
            break
if booll == False:
    print('-1') """

#2
""" some_list=[input('введите строку: ') for _ in range(int(input('ввкдите количество элементов')))]
el=input('введите искомое число: ')
C=0
if some_list.count(el)<2:
    print(-1)
else:
    for i in range(len(some_list)):
        if some_list[1]==el:
            c+=1
        if c==2:
            print(i)
            break
 """
#2
""" list_0 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
el = "qwe"
try:
    print(list_0.index(el,(list_0.index(el,len(list_0))),+1,len(list_0)))
except:
    print(-1) """

#3
""" some_list=[input('введите строку: ') for _ in range(int(input('ввкдите количество элементов')))]
el=input('введите искомое число: ')
first=some_list.index(el)
second=some_list.index(el, first+1)
print(second) """

#4
""" some_list=[input('введите строку: ') for _ in range(int(input('ввкдите количество элементов')))]
el=input('введите искомое число: ')
try: #обработчик ошибок
    print(some_list.index(el, some_list.index(el)+1))
except:
    print(-1) """

#files
with open('17.txt','w') as d:
    d.write('2')
