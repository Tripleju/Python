
import user_interface as us_int
import excep as ex
import model_mult as model_mult
import model_sum as model_sum
import model_pow as model_pow
import model_div as model_div
import model_sqrt as model_sqrt
import model_sub as model_sub
import sys
import logg as l
import compl as compl

def button_click():
    welcome=us_int.welcome()
    if welcome==0:
        print("Good bye, see you later!")
        exit()
    elif welcome==1:

            model=us_int.ch_operation()
            if model!='break':
                if model==model_div:
                    d=us_int.ch_div_op()
                else:
                    d=''
                value_a=us_int.get_value()
                value_b=us_int.get_value()
                while ex.division_zero(model,value_b)==False:
                    value_b=us_int.get_value()
                model.init(value_a, value_b)
                result=model.do_it(d)
                sym=model.symb(d)
                us_int.view_data(result, 'result')
                l.result_logger(value_a,value_b,sym,result)
            else: button_click()

    elif welcome==2:
        model=us_int.ch_operation()
        if model!='break':
            if model==model_div:
                d='/'
            else:
                d=''
            compl_values=us_int.get_complex_value()
            while ex.complex_div_zero(model, compl_values)==False:
                compl_values=us_int.get_complex_value()
                value_a=compl_values[0]
                value_b=compl_values[1]
            model.init(value_a, value_b)
            result=model.do_it(d)
            sym=model.symb(d)
            us_int.view_data(result, 'result')
            l.result_logger(value_a,value_b,sym,result)
        else: button_click()
    else:
        print("Wrong values")
        exit()
button_click()
#другой вариант записи. какой лучше?
def button_click1():
    welcome=us_int.welcome()
    if welcome==0:
        print("Good bye, see you later!")
        exit()
    elif welcome==1 or welcome==2:
            model=us_int.ch_operation()
            if model!='break':
                if model==model_div:
                    if welcome==1:
                        d=us_int.ch_div_op()
                    elif welcome==2:
                        d='/'
                else:
                    d=''
                if welcome==1:
                    value_a=us_int.get_value()
                    value_b=us_int.get_value()
                    while ex.division_zero(model,value_b)==False:
                        value_b=us_int.get_value()
                elif welcome==2:
                    compl_values=us_int.get_complex_value()
                    while ex.complex_div_zero(model, compl_values)==False:
                        compl_values=us_int.get_complex_value()
                        value_a=compl_values[0]
                        value_b=compl_values[1]
                model.init(value_a, value_b)
                result=model.do_it(d)
                sym=model.symb(d)
                us_int.view_data(result, 'result')
                l.result_logger(value_a,value_b,sym,result)
            else: button_click1()
    else:
        print("Wrong values, please try again")
        exit()
# button_click1()