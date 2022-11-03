# a- дописывать в существующий файл
# r - открытие для чтения данных
# w - открытие для записи данных
# w+ миксы
# r+

# colors=['red', 'green','blue']
# data=open('file.txt','a')
# data.writelines(colors)
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()

# with open('file.txt','w') as data: #при таком вызове можно напрямую не закрывать файл
#     data.write('\nLINE 2\n')
#     data.write('LINE 3\n')
#exit() пишем, что бы следующие строки незакомментированные не выполнялись

# path='file.txt'
# data=open(path, 'r')
# for line in data:
#     print(line)
# data.close()

#функции

# def f(x):
#  return x**2
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# import function_file
# print(function_file.f(1)) # Целое
# print(function_file.f(2.3)) # 23
# print(function_file.f(28)) # None


# def new_string(symbol, count=3):
#     return symbol * count
#print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12
#print(new_string('!')) # TypeError missing 1 required ...

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# рекурсия
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

#Кортеж – это неизменяемый “список”
# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e) # red green blue
#t[0] = 'black' # TypeError: 'tuple' object does not support
#item assignment

#словари: Неупорядоченные коллекции произвольных объектов с доступом по ключу
# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)

# for v in dictionary:
#     print(dictionary[v])


# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

#Множества

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}

# a = {1, 2, 3, 5, 8}
# b = frozenset(a) # неизменяемое множество
# print(b) # frozenset({1, 2, 3, 5, 8})

# списки дополнение
#так не копируем списки
# list1=[1,2,3,4,5]
# list2=list1

# list1[0]=123
# list2[1]=333

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# удаление элементов

list1=[1,2,3,4,5]

# print(len(list1))
# print(list1.pop()) #удаление последнего элемента
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# print(list1.pop(2)) #удаление выбранного элемента
# print(list1)

# print(list1.insert(3,11)) #вставка элемента на выбранное место
# print(list1)

# print(list1.append(11)) #добавление элемента в конец
# print(list1)
