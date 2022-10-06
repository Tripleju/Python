""" 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 """

##num=float(input('введите число: '))
#comma='.'
#for i in len(num):
#print(str(num).count(str(comma)))
#if str(num).index('.')!=len(str(num))-2:
##new_num=int(str(num).replace('.',''))
#else:
#    num_new=num

""" str_new=" ".join(num_new)
list_new=str_new.split()
for i in len(list_new): """

# sum = 0
# while (new_num != 0):
#     sum = sum + new_num % 10
#     new_num = new_num // 10
# print("Сумма цифр числа равна: ", sum)

#print(list_new)
""" print(len(str(num)))
print(str(num).index('.'))
print(num_new) """


print("gipopotapo".count("po",3,5)) #можно задавать диапазон поиска


#3 вариант задачи 1 (не работает)
# num=float(input('введите число: '))
# new_num=(str(num).replace('.',''))
# str_new=" ".join(new_num)
# list_new=str_new.split()
# print("Сумма цифр числа равна: ", sum(int(list_new)))