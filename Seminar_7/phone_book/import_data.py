import csv

# def import_table():
#     with open('phone_book.csv', newline='') as File:  
#         reader = csv.reader(File)
#         for row in reader:
#             print(row)
def import_table():
    with open('phone_book.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)