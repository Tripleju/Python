# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых 
# больше предыдущего элемента. Use comprehension.
""" in
9
out
[15, 16, 2, 3, 1, 7, 5, 4, 10]
[16, 3, 7, 10]

in
10
out
[28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
[24, 15, 23, 25] """
#вариант 1 мой
# from random import sample
# def bigger_first(num:int):
#     first_list=((sample([i for i in range(num*3)],k=num)))
#     # first_list=sample(range(num*3),num) #как вариант записи
#     print(first_list)       
#     short_list=[first_list[j] for j in range(1,num-1) if first_list[j]>first_list[j-1]]
#     print(short_list)
# bigger_first(int(input("enter number: ")))

#вариант 2
# from random import randint
# def more_then(num):
#     original_list=[randint(0,1000) for _ in range(num)]
#     print(original_list)
#     return [num for i in enumerate(original_list[1:]) if num > original_list[i]]

# print(more_then(int(input('enter number: '))))
#TypeError: list indices must be integers or slices, not tuple

# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
""" in
100
out
[20, 21, 40, 42, 60, 63, 80, 84, 100]

in
424
out
[20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]
 """

# def multiple(N:int):
#     my_list=[x for x in range(20,N+1) if (x%20==0 or x%21==0)]
#     return my_list

# print(multiple(int(input('enter number: '))))














#3 get setdefault