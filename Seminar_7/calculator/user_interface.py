
from numbers import Complex, Rational
from subprocess import CompletedProcess
import model_mult as model
import user_interface as us_int




def view_data(data, title):
    print(f'{title}={data}')

def get_value():
    return int(input('value= '))


def welcome():
    print("Calculator welcomes you!")
    print(" Working with:\n 1 - Rational \n 2 - Complex\n 0 - exit")
    return input("Please choose option: ")

def ch_operation():
    operation=input("Choose operation:\n 1 - sum\n 2 - sub\n 3 - mult\n 4 - div\n 5 - pow\n 6 - sqrt\n 0 - previouse menu")
    return operation
    



