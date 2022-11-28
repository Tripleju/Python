import user_interface as us_int
import model_div as model_div
import model_sqrt as model_sqrt


def check_digit(value,num):
    if value.isdigit()==False:
        print("Yyoops! Something going wrong! please enter number!")
    elif value>num:
        print("Enter the number in range above")


def check_value(value):
    if value.replace(".","",1).replace("-","",1).isdigit()==False:
        print("Yoops! Something are going wrong! please enter the number!")
        del value
        return False
    else: return True

def division_zero(model, value):
    if (model==model_div or model==model_sqrt) and value==0:
        print("Division by zero, plese try again")
        del value
        return False
    else: return True

def complex_div_zero(model, value):
    if (model==model_div or model==model_sqrt) and value[1]==complex(0,0):
        print("Complex division by zero, plese try again")
        del value
        return False
    else: return True

def check_operations(value:str, num):
    if value.isdigit()==False: 
        print("Yoops! Something are going wrong! please choose from the listed option!")
        return False
    elif int(value) not in range(1,num+1):
        print("Yoops! Something are going wrong! please choose from the listed option!")
        return False    
    else: True


