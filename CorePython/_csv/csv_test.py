import csv

"""
# Write on CSV File
with open("data1.csv", 'w', newline='') as csv_file: # Create a blank _csv file
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['ID','NAME','ADDRESS'])# Heading Row
    csv_writer.writerow([1, 'Anupam Neupane', 'Bhk']) # Data Row
    csv_writer.writerow([2, 'Arjun Bhattarai', 'Lat'])
    csv_writer.writerow([3, 'Bibek Rawat', 'Ktm'])
    csv_writer.writerow([4, 'Dinesh Tharu', 'Ktm'])
    csv_writer.writerow([5, 'Puskar Karki', 'Lat'])
    csv_writer.writerow([6, 'Rupesh Shrestha', 'Bhk'])
    csv_writer.writerow([7, 'Sachin Kr Shrestha', 'Ktm'])

# Read from CSV File
with open("data1.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    persons = []
    for r in csv_reader:        
        persons.append(r)
                
for person in persons:
    print(person)

# DictWriter/DictReader
# Writer
with open("data2.csv", "w", newline='') as csv_file:
    field_names = ("SN","NAME","ADDRESS")
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'SN': 1,'NAME':'Arjun','ADDRESS':'KTM'})
    writer.writerow({'SN': 2, 'NAME': 'Sachin', 'ADDRESS': 'LAT'})
    writer.writerow({'SN': 3, 'NAME': 'Rajiv', 'ADDRESS': 'BHK'})
"""

# Reader
with open('data2.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(dict(row))