from datetime import datetime as dt
from time import time
# from prettytable import from_csv

def data_save(data):
    time=dt.now().strftime('%d/%m/%y %H:%M')
    with open('phone_book.csv', 'a',encoding='utf-8') as hist_file:
        hist_file.write('{};{};{};{};{}\n'
                    .format(time,data[0],data[1],data[2],data[3]))
    


# def table_data(data):