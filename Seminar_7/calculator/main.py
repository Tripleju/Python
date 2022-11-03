
import user_interface as us_int

import model_mult as model_mult
import model_sum as model_sum
import model_pow as model_pow
import model_div as model_div
import model_sqrt as model_sqrt
import model_sub as model_sub
import sys
import logg as l

def button_click():
    # us_int.welcome()
    # if us_int.welcome()==0:
        # sys.exit('Good bye')
    # else:
        model=us_int.ch_operation()
        if model!='break':
            if model==model_div:
                d=us_int.ch_div_op()
            else:
                d=''
            value_a=us_int.get_value()
            value_b=us_int.get_value()
            model.init(value_a, value_b)
            result=model.do_it(d)
            sym=model.symb(d)
            us_int.view_data(result, 'result')
            l.result_logger(value_a,value_b,sym,result)
        else: button_click()

button_click()

