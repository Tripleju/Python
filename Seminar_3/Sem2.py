# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая определит, присутствует ли в заданном списке число,
# полученное от пользователя.

# from random import sample
# def num_in_list(count, number):
#     if count<0:
#         return "error"
#     list=sample(range(1, count*2), count)
#     print(list)
#     if number in list:
#         return "yes"
#     return "no"

# print(num_in_list(int(input()), int(input())))


# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.

from random import choices
def list_new(n, word):
    new_list=[]
    for i in range(n):
        a=choices(word,k=3) #выбирает из списка k случайных элементов в произвольном порядке
        new_list.append(''.join(a)) #слепляет вместе без пробела
    return new_list



def find_word(my_list,word_find):
    if my_list.count(word_find)>1:
        print('yes')
        n=my_list.index(word_find)
        print(my_list.index(word_find,n+1))
    else:
        print(-1)

result=list_new(15,"abc")

print(result)

find_word(result,input())