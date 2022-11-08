
def input_data():
    surname=input("Enter surname: ")
    name=input("Enter name: ")
    position=input("Enter position: ")
    contr_type=input("Enter contract_type: ")
    return [surname, name, position, contr_type]


def welcome():
    option=int(input("Hello! what do you like to do now?\n Choose the option:\n 1 - look to the data\n 2 - filter data\n 3 - input new data\n 4 - exit\n "))
    return option