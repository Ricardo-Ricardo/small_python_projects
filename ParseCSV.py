import csv

with open('names.csv', 'r') as csv_file: #open original file
    csv_reader = csv.DictReader(csv_file) # read original file

    #next(csv_reader) # skips the first line
    with open('new_names.csv', 'w') as new_file: # open new file
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter = '\t') # adds a tab to each line instead of comma

        csv_writer.writeheader()

        for line in csv_reader: # reads each line
            del line['email']
            csv_writer.writerow(line) # write out each new line
