import csv


def show_data():
#     with open('main data.csv','a', newline='',encoding='utf-8') as File:  
#         reader = csv.reader(File)
#         for row in reader:
#             print(row)


    # results = []
    with open('main data.csv', encoding='utf-8') as File:
        headers=["id","Surname","Name","Position","Contract_type"]
        reader = csv.DictReader(File, headers, delimiter=";")
        for row in reader:
            print(row)