
import user_interface as us_int
import model_mult as model
import logg as l

def button_click():
    us_int.welcome()
    value_a=us_int.get_value()
    value_b=us_int.get_value()
    model.init(value_a, value_b)
    result=model.do_it()
    sym=model.symb()
    us_int.view_data(result, 'mult')
    l.result_logger(value_a,value_b,sym,result)

button_click()

