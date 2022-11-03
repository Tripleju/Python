# 5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

""" in
10 True
out
['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый', 'город позавчера утопичный']
in
10 False
['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый', 'город вчера утопичный', 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый', 'огонь позавчера яркий', 'огонь где-то утопичный', 'автомобиль где-то мягкий'] """

from random import choice, randrange

def some_jokes(n:int, repeat:bool=False)-> list:
    """ 
    Функция возвращает случайные шутки, собранные из 3х списков слов 
    :param n: количество шуток
    :param repeat: уникальны\неуникальные
    :return: список случайных шуток

    """
    no, adv, adj=nouns.copy, adverbs.copy, adjectives.copy
    list_of_j=[]
    list_min=min(no,adv,adj)

    for i in range(len(list_min) % n if repeat else n):
        num=randrange(len(list_min))
        list_of_j.append(f"{no.pop(num)}{adv.pop(num)}{adj.pop(num)}" if repeat
                        else f"{choice(nouns)}{choice(adverbs)}{choice(adjectives)}")
    return list_of_j

print(some_jokes(100, True))
# print(help(some_jokes))
# print(some_jokes,__doc__)

# =>>  File "c:\Users\Юля\Desktop\git_edu\Python\Python\Seminar_6\HW_5.py", line 26, in some_jokes
#     list_min=min(no,adv,adj)
# TypeError: '<' not supported between instances of 'builtin_function_or_method' and 'builtin_function_or_method'



