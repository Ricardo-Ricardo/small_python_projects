import csv

with open('names.csv', 'r') as csv_file: #open original file
    csv_reader = csv.reader(csv_file) # read original file

    #next(csv_reader) # skips the first line
    with open('new_names.csv', 'w') as new_file: # open new file
        csv_writer = csv.writer(new_file, delimiter = '-') # adds a dash to each line instead of comma

        for line in csv_reader: # reads each line
            csv_writer.writerow(line) # wirte out each new line
