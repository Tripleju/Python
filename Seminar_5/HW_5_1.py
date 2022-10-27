# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
""" Number of words: 10
out
авб абв бав абв вба бав вба абв абв абв
авб бав вба бав вба

in
Number of words: 6
out
ваб вба абв ваб бва абв
ваб вба ваб бва

in
Number of words: -1
out
The data is incorrect """

from random import sample
def create_first_str(num:int, word):
    if num<=0:
        print('The data is incorrect')
        return ''
    first_list=[]
    for i in range(num):
        a=sample(word,k=3)
        first_list.append(''.join(a))
        first_str=" ".join(first_list)
    return first_str

first_string=create_first_str(int(input("Введите количество элементов списка: ")),'абв')
print(first_string)

def delete_word(word:str, my_string:str):
    if my_string=='':
        return ''
    final_list=[x for x in my_string.split() if x != word]
    final_str=" ".join(final_list)
    return final_str

print(delete_word('абв', first_string))







