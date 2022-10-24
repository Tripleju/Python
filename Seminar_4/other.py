#2
from math import sqrt
def simple_prod_list(num):
    list_simple=[]
    for i in range(2,int(sqrt(num))):
        if num%i!=0:
            list_simple.append(num)
        
    print(list_simple)
simple_prod_list(my_num)