import os

def read_files_in_path(path):
    os.chdir(path)

    filenames = os.listdir()

    return filenames


input_path = r'/Users/danielsilva/Documents/Onboarding/Python Scripting'
result = read_files_in_path(input_path)

print(type(result))
print(result)
