import csv

with open('testwritecsv.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Roll']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
     
    writer.writeheader()
    writer.writerow({'Roll': '11', 'first_name': 'Albert', 'last_name': 'Dsouza'})
    writer.writerow({'Roll': '22', 'first_name': 'Frank',
                     'last_name': 'Rodriguez'})
    writer.writerow({'Roll': '33', 'first_name': 'Maria', 'last_name': 'Parker'})

print("Writing complete")
