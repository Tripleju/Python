""" 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
*Пример:*
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} """

#1
""" N=int(input('введите число: '))
dictionary = {}
dictionary = { i: 3*i+1 for i in range(1, N+1)}
print(dictionary) """

#2
# n=int(input())
# some_dict={}
# for i in range(1,n+1):
#     some_dict[i]=3*i+1
# print(some_dict)

# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
# где k принимает значения от 1 до n включительно.

numbers = []
count = int(input('Write count numbers: '))
for i in range(1, count+1):
numbers.append(3*i +1)

print(numbers)