# 1. Вычислить число c заданной точностью d
#1 var
# from decimal import Decimal

# def accuracy(num, acc):
#     number = Decimal(f"{num}")
#     return number.quantize(Decimal(f"{acc}"))

# print(accuracy(float(input("Enter a real number: ")), float(input("Enter the required accuracy 0.0001: "))))

#2 var
# num=float(input('Enter a real number: '))
# _,accu=input('Enter a reaquered accuracy "0.0001": ').split('.')
# print(f'{num:.{len(accu)}f}')

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def find_prime_nums(num):
#     pr_fact=[]
#     di=2
#     while num>1:
#         if num%di==0:
#             pr_fact.append(di)
#             num//=di
#         else:
#             di+=1
#     return pr_fact

# print(find_prime_nums(int(input('enter number: '))))

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

from random import randrange
def list_rand_numb(n:int):
    if n<0:
        print('Negative value of the number of numbers!')
        return []
    first_list=[]
    for i in range(n):
        first_list.append(randrange(n))
    return first_list

def uniq_el(first_list:list):
    result=[]
    my_dict={}.fromkeys(first_list,0)

    for i in first_list:
        my_dict[i]+=1

    for k in my_dict:
        if my_dict[k]==1:
            result.append(k)

    return result

all_list=list_rand_numb(int(input("Number of numbers: ")))
print(all_list)
print(uniq_el(all_list))
    
        
