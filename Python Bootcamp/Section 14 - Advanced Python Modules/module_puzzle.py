import re
import os

file_location = 'C:/Users/jerry/OneDrive/Section 14 - Advanced Python Modules/extracted_content/'
pattern = r'\d{3}-\d{3}-\d{4}'

info = []
for folder, sub_folders, files in os.walk(file_location):
    for f in files:
        full_path = folder + "//" + f
        f = open(full_path, 'r')
        read = f.read()
        check = re.search(pattern, read)
        if check is not None:
            print(check.group())
