from datetime import datetime as dt
from time import time

def result_logger(value_a, value_b,symbol,result):
    time=dt.now().strftime('%d/%m/%y %H:%M')
    with open('log_calc.txt', 'a') as file:
        file.write('data: {}; calculation: {} {} {}= {}\n'
                    .format(time,value_a,symbol,value_b,result))
