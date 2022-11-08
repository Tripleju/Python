import csv
 
# with open('example4.csv', 'w') as csvfile:
#     fieldnames = ['first_name', 'last_name', 'Grade']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
#     writer.writeheader()
#     writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
#     writer.writerow({'Grade': 'A', 'first_name': 'Rachael',
#                      'last_name': 'Rodriguez'})

# print("Writing complete")


 
results = []
with open('main data.csv', encoding='utf-8') as File:
    headers=["id","Surname","Name","Position","Contract_type"]
    reader = csv.DictReader(File, headers, delimiter=";")
    for row in reader:
        # for row in reader:
        print(row)

    #     results.append(row)
    # print(results)