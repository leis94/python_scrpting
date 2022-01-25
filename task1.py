import os
import re
import argparse
from time import perf_counter


def read_files_in_path(filenames):
    if len(filenames) == 1:
        filename = filenames[0]
        try:
            for i, line in enumerate(open(filename)):
                for match in re.finditer(pattern, line):
                    #print('Found on line %s: %s' % (i+1, match.group()))
                    print(
                        f'File name: {filename}, Found on line {i+1}: {match.group()}')
        except IsADirectoryError as e:
            pass

    else:
        mid = len(filenames) // 2
        first_half = filenames[:mid]
        second_half = filenames[mid:]

        read_files_in_path(first_half)
        read_files_in_path(second_half)


parser = argparse.ArgumentParser()
parser.add_argument("path", help="Path where looking into content files.")
parser.add_argument("re", help="Regex Patter to match into content files.")
args = parser.parse_args()
pattern = re.compile(args.re)
os.chdir(args.path)
filenames = os.listdir()
# Start the stopwatch / counter
t1_start = perf_counter()
read_files_in_path(filenames)
# Stop the stopwatch / counter
t1_stop = perf_counter()
print("Elapsed time:", t1_stop, t1_start)
