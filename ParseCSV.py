import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader) # skips the first line
    for line in csv_reader:
        print(line[2])
