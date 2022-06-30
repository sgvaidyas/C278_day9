import csv
with open('testCSV2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'emp_name': 'Alice', 'dept': 'Accounting'})
    writer.writerow({'emp_name': 'Shweta', 'dept': 'IT'})
