import save_data as s
from os import path 

def add_new_contacts(file_name: str):
    if path.exists(file_name):
        with open(file_name, 'r') as fn:
            new_file = fn.read()
    else:
        print("File name does not exist in the system")

    with open('phone_book.csv', 'a') as hist_file:
        # hist_file.write('\n')
        hist_file.write(new_file)
    print("data was added to the main book")