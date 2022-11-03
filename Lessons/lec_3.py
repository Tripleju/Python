#def sum(x,y):
#    return x+y

# f=sum

""" def mylt (x,y):
    return x*y

def calc(op,a,b):
    print(op,(a,b))
    #return op(a,b) """

# calc(mylt, 4,5)
# calc(f, 4,5)

""" sum=lambda x, y: x+y
calc(sum, 4,5) """

""" calc(lambda x, y: x+y, 4,5) """

#список из нечетных чисел
#1
""" list[]
for i in range(1,101):
    if(i%2==0):
        list.append(i):

print(list) """


#2
""" list= [i for i in range(1,101) if i%2==0]
print(list)
 """
#список кортежей
""" list= [(i,i) for i in range(1,101) if i%2==0]
print(list) """

# пара число и его куб
""" def f(x):
    return x**3
list= [(i,f(i)) for i in range(1,21) if i%2==0]
print(list) """

#пара число и его квадрат с использованием лямбды
""" sqr=lambda i: i**2
list= [(i,sqr) for i in range(1,21) ]
print(list) """

#1

""" path = 'C:/Users/Юля/Desktop/git_edu/Python/17.txt'
f=open(path,'r')
data=f.read()+' ' #считываем в все что есть и добавляем пробел
f.close()

numbers=[]

while data !='':
    space_pos=data.index(' ')
    numbers.append(int(data[:space_pos]))
    data=data[space_pos+1:]

out=[]
for e in numbers:
    if not e%2:
        out.append((e,e**2))
print(out) """

#2 тоже но оптимизированное
# def select(f,col):
#     return [f(x) for x in col]

# def where(f,col):
#     return [x for x in col if f(x)]

# data='1 2 3 5 8 15 23 38'.split()
# res=select(int,data)

# res=where(lambda x: not x%2, res)
# res=select(lambda x:(x,x**2), res)
# print(res)

#map

# li=[x for x in range(1,20)]

# li=list(map(lambda x:x+10, li))

# print(li)

# data=list(map(int(input().split())))
# print(data)


# data=list(map(int,'1 2 3 555 7'.split()))
# for e in data:
#     print(e)

# print('---')
# for e in data:
#     print(e)

#3 тоже но с map
# def map(f,col):
#     return [f(x) for x in col]

# def where(f,col):
#     return [x for x in col if f(x)]

# data='1 2 3 5 8 15 23 38'.split()
# res=map(int,data)

# res=where(lambda x: not x%2, res)
# res=list(map(lambda x:(x,x**2), res))
# print(res)

#filter()

# data=[x for x in range(10)]
# # res=list(filter(lambda x:x%2==0,data))
# res=list(filter(lambda x:not x%2,data))
# print(res)

#4 тоже но с filter
# def map(f,col):
#     return [f(x) for x in col]

# def filter(f,col):
#     return [x for x in col if f(x)]

# data='1 2 3 5 8 15 23 38'.split()
# res=map(int,data)

# res=filter(lambda x: not x%2, res)
# res=list(map(lambda x:(x,x**2), res))
# print(res)

#функция zip
# users=['user1', 'user2', 'user3', 'user4', 'user5']
# ids=[4,5,9,11,7]
# salary=[111,222,333]

# data=list(zip(users, ids, salary))
# print(data)

#функция enumerate

# users=['user1', 'user2', 'user3', 'user4', 'user5']
# ids=[4,5,9,11,7]
# salary=[111,222,333]

# data=list(enumerate(users))
# print(data)

