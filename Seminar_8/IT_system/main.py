import interface as int
import show_data as show
import add_data as add

def button_click():
    welcome=int.welcome()
    if welcome==4:
        print("Good bye, see you later!")
        exit()
    if welcome==1:
        show.show_data()
    # if welcome==2:
    #     file_name=int.export()
    #     exp.add_new_contacts(file_name)

    if welcome==3:
        add.input_data()
    else:
        print("please enter number from listed options")
        button_click()


button_click()