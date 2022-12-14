
from numbers import Complex, Rational
from subprocess import CompletedProcess
import user_interface as us_int
import model_mult as model_mult
import model_sum as model_sum
import model_pow as model_pow
import model_div as model_div
import model_sqrt as model_sqrt
import model_sub as model_sub
import excep as ex




def view_data(data, title):
    print(f'{title}={data}')

def get_value():
    value=(input('value= '))
    while ex.check_value(value)==False:
        del value
        value=(input('value= '))
    return float(value)



def welcome():
    print("Calculator welcomes you!")
    print(" Working with:\n 1 - Rational \n 2 - Complex\n 0 - exit")
    return int(input("Please, choose the option: "))

def ch_operation():
    operation=(input("Choose operation:\n 1 - sum\n 2 - sub\n 3 - mult\n 4 - div\n 5 - pow\n 6 - sqrt\n 7 - previouse menu\n" ))
    # dict_operation=dict([(1,'sum'),(2,'sub'),(3,'mult'),(4,'div'),(5,"pow"),(6,'sqrt'),(0,'previose menu')])
    dict_models=dict([(1,model_sum),(2,model_sub),(3,model_mult),(4,model_div),(5,model_pow),(6,model_sqrt),(7,"break")])
    while ex.check_operations(operation,len(dict_models))==False:
        del operation
        operation=(input("Choose operation:\n 1 - sum\n 2 - sub\n 3 - mult\n 4 - div\n 5 - pow\n 6 - sqrt\n 7 - previouse menu\n" ))
        dict_models=dict([(1,model_sum),(2,model_sub),(3,model_mult),(4,model_div),(5,model_pow),(6,model_sqrt),(7,"break")])
    return dict_models.get(int(operation))
    
def ch_div_op():
    operation1=(input("Choose operation:\n 1 - / \n 2 - // \n 3 - % \n" ))
    dict_div=dict([(1,'/'),(2,'//'),(3,'%')])
    while ex.check_operations(operation1,len(dict_div))==False:
        del operation1
        operation1=(input("Choose operation:\n 1 - / \n 2 - // \n 3 - % \n" ))
        dict_div=dict([(1,'/'),(2,'//'),(3,'%')])
    return dict_div.get(int(operation1))


def get_complex_value():
    real_part1=(input('Enter 1 real part: '))
    while ex.check_value(real_part1)==False:
        del real_part1
        real_part1=(input('Enter 1 real part: '))
    im_part1=(input('Enter 1 imaginary part: '))
    while ex.check_value(im_part1)==False:
        del im_part1
        im_part1=(input('Enter 1 imaginary part: '))
    real_part2=(input('Enter 2 real part: '))
    while ex.check_value(real_part2)==False:
        del real_part2
        real_part2=(input('Enter 2 real part: '))
    im_part2=(input('Enter 2 imaginary part: '))
    while ex.check_value(im_part2)==False:
        del im_part2
        im_part2=(input('Enter 2 imaginary part: '))
    value1= complex(float(real_part1),float(im_part1))
    value2= complex(float(real_part2),float(im_part2))
    print(f"value 1= {value1}")
    print(f"value 2= {value2}")
    return [value1, value2]






