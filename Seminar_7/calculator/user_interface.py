
from numbers import Complex, Rational
from subprocess import CompletedProcess
import user_interface as us_int
import model_mult as model_mult
import model_sum as model_sum
import model_pow as model_pow
import model_div as model_div
import model_sqrt as model_sqrt
import model_sub as model_sub





def view_data(data, title):
    print(f'{title}={data}')

def get_value():
    return int(input('value= '))


def welcome():
    print("Calculator welcomes you!")
    print(" Working with:\n 1 - Rational \n 2 - Complex\n 0 - exit")
    return input("Please choose option: ")

def ch_operation():
    operation=int(input("Choose operation:\n 1 - sum\n 2 - sub\n 3 - mult\n 4 - div\n 5 - pow\n 6 - sqrt\n 0 - previouse menu\n" ))
    # dict_operation=dict([(1,'sum'),(2,'sub'),(3,'mult'),(4,'div'),(5,"pow"),(6,'sqrt'),(0,'previose menu')])
    dict_models=dict([(1,model_sum),(2,model_sub),(3,model_mult),(4,model_div),(5,model_pow),(6,model_sqrt),(0,"break")])
    return dict_models.get(operation)
    
def ch_div_op():
    operation1=int(input("Choose operation:\n 1 - / \n 2 - // \n 3 - % \n" ))
    dict_div=dict([(1,'/'),(2,'//'),(3,'%')])
    return dict_div.get(operation1)




