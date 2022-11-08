import csv

def input_data():
    surname=input("Enter surname: ")
    name=input("Enter name: ")
    position=input("Enter position: ")
    contr_type=input("Enter contract_type: ")
    # return [surname, name, position, contr_type]

    with open('main data.csv', 'a', encoding='utf-8') as csvfile:
        headers=["id","Surname","Name","Position","Contract_type"]
        writer = csv.DictWriter(csvfile, fieldnames=headers,delimiter=";")
    
        # writer.writeheader()
        writer.writerow({'id': '5', "Surname": surname, "Name": name,"Position":position,"Contract_type": contr_type})
        

        print("Writing complete")
