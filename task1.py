import os
import re


def read_files_in_path(filenames):
    if len(filenames) == 1:
        filename = filenames[0]
        try:
            for i, line in enumerate(open(filename)):
                for match in re.finditer(pattern, line):
                #print('Found on line %s: %s' % (i+1, match.group()))
                    print(f'File name: {filename}, Found on line {i+1}: {match.group()}')
        except IsADirectoryError as e:
            pass

    else:
        mid = len(filenames) // 2
        first_half = filenames[:mid]
        second_half = filenames[mid:]

        read_files_in_path(first_half)
        read_files_in_path(second_half)


input_path = r'/Users/danielsilva/Documents/Onboarding/Python Scripting'
pattern = re.compile('[0-9]+')
os.chdir(input_path)
filenames = os.listdir()
print(filenames)
read_files_in_path(filenames)