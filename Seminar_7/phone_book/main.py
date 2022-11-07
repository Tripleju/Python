import interface as int
import import_data as imp
import export_data as exp
import save_data as s

def button_click():
    welcome=int.welcome()
    if welcome==4:
        print("Good bye, see you later!")
        exit()
    if welcome==1:
        data=int.input_data()
        s.data_save(data)
    if welcome==2:
        file_name=int.export()
        exp.add_new_contacts(file_name)

    # if welcome==3:
    #     imp.import_table()
    else:
        print("please enter number from listed options")
        button_click()

button_click()