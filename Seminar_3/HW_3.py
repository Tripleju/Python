# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list=[2,3,5,9,3]
# from random import sample
# def list_rand_nums(count:int):
#     if count<0:
#         print('отрицательное число количесва элементов')
#         return []

#     list_nums=sample(range(1,count*2),count)
#     return list_nums

# def sum_el(some_list):
#     s=0
#     for i in range(0,len(some_list),2):
#         s+=some_list[i]

#     print(s)

# sum_el(my_list)


# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 4];
# - [2, 3, 5, 6] => [12, 15]

# my_list1=[2, 3, 4, 5, 6]
# my_list2=[2, 3, 5, 6]

# def prod_pair(some_list):
#     prod_list=[]
#     len_list=int(len(some_list))
#     for i in range(int(len_list/2)):
#         prod_p=some_list[i]*some_list[len_list-i-1]
#         prod_list.append(prod_p)
#     if len_list%2!=0:
#         av_el=some_list[int(len_list/2)]
#         prod_list.append(av_el)

#     print(prod_list)

# prod_pair(my_list2)
# prod_pair(my_list1)





# 4*. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import uniform

# def list_rand_nums(count: int):
#     list_nums=[]
#     if count<=0:
#         print('Negative value of the number of numbers!')
#         return [0.0]

#     for i in range(count):
#         list_nums.append(round(uniform(1,count),2))
#     return list_nums

# def dif_max_min(list_nums: list):
#     num_max=num_min=list_nums[0]%1

#     for k in range(1,len(list_nums)):
#         num=round(list_nums[k]%1,2) # %1 убирает целую часть, оставлят только дробную.
#         if num>num_max:
#             num_max=num
#         elif num<num_min:
#             num_min=num
    
#     result=round(num_max-num_min,2)
#     print(f"Min: {num_min}, Max: {num_max}, Difference: {result}")
#     return result #если не добавить return, то функция не возвращет ничего и дальше с результатом работать нельзя

# all_list=list_rand_nums(int(input('Number of numbers: ')))
# print(all_list)
# print(dif_max_min(all_list))


# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# my_num=int(input('введите число: '))
# def dec_to_bin(num):
#     bin_list=[]
#     while num!=0:
#         rem=num%2
#         bin_list.append(rem)
#         num=num//2
#     bin_list.reverse()   
#     print("".join(map(str,bin_list)))

# dec_to_bin(my_num)

#2 вариант решения (схитрили и то что получается не является числом, просто выглядит)
# def conv_bin(num: int):
#     list_nums = []

#     while num > 0:
#         list_nums.insert(0, num % 2)
#         num //= 2

#     print(*list_nums, sep="") #* значит разпаковка списка и указываем формально, что сепаратор между числами пустой

# conv_bin(int(input()))

# 5**. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи]
# (https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)

def neg_fib(num: int):
    a, b = 1, 1
    list_nums = [0]

    for i in range(num):
        list_nums.append(a)
        list_nums.insert(0, a * (-1) ** i)
        a, b = b, b + a

    return list_nums

print(*neg_fib(int(input())))