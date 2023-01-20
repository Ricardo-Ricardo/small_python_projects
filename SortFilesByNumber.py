### this script is an example of sorting files by renaming them

# Example files to sort:
# Earth - Our Solar System - #4.mp4
# The Sun - Our Solar System - #1.mp4
# Venus - Our Solar System - #3.mp4
# Mercury - Our Solar System - #2.mp4

import os

# Use directory where all the files are stores
os.chdir('/Users/ricky/Desktop/Videos')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) # tuple of the name and the type of file/extension
    if (f_ext == ".mp4"): # checks the file type so only wanted files are changed
        f_title, f_course, f_num = f_name.split('-') #tuple of the 3 sections, title, course, and number

        f_title = f_title.strip()
        f_course = f_course.strip()
        f_num = f_num.strip()[1:].zfill(2) # zero padded string so 10 won't be before 2
        
        new_name = ('{}-{}{}'.format(f_num, f_title, f_ext))

        os.rename(f, new_name) # renames files to new format
    else:
        continue # continues if unwanted file is found


