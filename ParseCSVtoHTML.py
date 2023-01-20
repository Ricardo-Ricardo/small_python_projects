### this script is an example of how to read, parse, and write to html

# example of csv file
# first_name,last_name,email,pledge,lifetime,status,country,start
# description "Add names with reward"
# John,Doe,john-doe@hotmail.com,10.00,20.00,ok,,2017-05-06 21:28:06.183108
# Chris,Smith,ChrisSmith@gmail.com,5.00,10.00,ok,,2017-05-29 16:13:58.318920
# No Reward,Description:(None)...
# Maggie,Jefferson,maggie-jefferson@aol.com,1.00,12.00,ok,,2016-07-26 05:02:16

import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file: # opens the file
    csv_data = csv.reader(data_file) # reads the file
    
    # skips the first and second line of bad data
    next(csv_data)
    next(csv_data)

    for line in csv_data: # go through each line in file
        if line[0] == "No Reward": # script will stop once it reaches no reward
            break
        names.append(f"{line[0]} {line[1]}") # adds first and second components

html_output += f'<p>There are currently {len(names)} contributors. Thank You!</p>' # use html paragraph tabs, add number of people

html_output += '\n<ul>' # unordered list

for name in names:
    html_output += f'\n\t<li>{name}<\li>' # add names to html list

html_output += '\n</ul>' # close list

print(html_output)