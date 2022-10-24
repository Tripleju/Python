# def conv_bin(num: int):
#     list_nums = []

#     while num > 0:
#         list_nums.insert(0, num % 2)
#         num //= 2

#     print(*list_nums, sep="")


# conv_bin(int(input()))


# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

#1
# line=input("введите список: ")
# list_1=[int(x.strip(',.*')) for x in line.split() if x.replace("-","").isdigit()]
# print(f'Min: {min(list_1)}, Max: {max(list_1)}')

#2 если используем формат строки
# line=input("введите список: ")
# list_1=[(x.strip(',.*')) for x in line.split() if x.replace("-","").isdigit()]
# print(f'Min: {min(list_1, key=int)}, Max: {max(list_1, key=int)}')

#2 распаковка
# list_1=[]
# for x in input().split():
#     if x.replace("-","").isdigit():
#         list_1.append(x.strip(',.*'))
# print(f'Min: {min(list_1, key=int)}, Max: {max(list_1, key=int)}')

#3
def check(str_list):
    for i, num in enumerate(str_list):
        str_list[i] = num.strip('.,;:?!')
        if not str_list[i].replace("-", "").isdigit():
            return []
    return str_list


def find_max_min(nums_str: str):
    list_nums = nums_str.split()
    right_list = check(list_nums)

    if right_list:
        return min(right_list, key=int), max(right_list, key=int)
    print("The data is incorrect")
    return []


print(*find_max_min(input("Enter the numbers separated by a space: ")))