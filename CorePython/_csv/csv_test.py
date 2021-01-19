import csv
"""
# Write on CSV File
with open("data1.csv", 'w') as csv_file: # Create a blank _csv file
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['ID','NAME','ADDRESS'])
    csv_writer.writerow([1, 'Anupam Neupane', 'Bhk'])
    csv_writer.writerow([2, 'Arjun Bhattarai', 'Lat'])
    csv_writer.writerow([3, 'Bibek Rawat', 'Ktm'])
    csv_writer.writerow([4, 'Dinesh Tharu', 'Ktm'])
    csv_writer.writerow([5, 'Puskar Karki', 'Lat'])
    csv_writer.writerow([6, 'Rupesh Shrestha', 'Bhk'])
    csv_writer.writerow([7, 'Sachin Kr Shrestha', 'Ktm'])
"""

# Read from CSV File
with open("data1.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    persons = []
    for record in csv_reader:
        if len(record)>0:
            persons.append(record)
    #print(persons)

for person in persons:
    print(person)
