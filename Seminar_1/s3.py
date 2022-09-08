#Александр LyraX: 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#*Примеры:*
#- 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

""" N=int(input('введите число: '))
A=[-N]
for i in range(2*N):
    A.append(-N+1)
    N=N-1
print(A) """

N=int(input())
for i in range(-N,N):
    print(i, end=',')
print(N)







