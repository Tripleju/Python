
def input_data():
    surname=input("Enter surname: ")
    name=input("Enter name: ")
    phone=input("Enter phone: ")
    descript=input("Enter description: ")
    return [surname, name, phone, descript]


def welcome():
    option=int(input("Hello! what do you like to do now?\n Choose the option:\n 1 - input data manually\n 2 - export data\n 3 - import data\n 4 - exit\n"))
    return option

def export():
    file_name=input("Please enter file name with new data with extention .csv:\n for test enter: 'phone_book_new.csv'\n ")
    print()
    return file_name

