import csv
import sys
import os

from tabulate import tabulate
from pathlib import Path

def main():
    input_file = check_cmd_argv(sys.argv)
    data = read_file_dict(input_file)
    print_data(data)

def print_data(data):
    print(tabulate(data, headers = "keys", tablefmt = "grid"))

def read_file_dict(input_path):
    data = {}
    with open(input_path, 'r') as file:
        for row in csv.DictReader(file):
            for key, element in row.items():
                if key not in data:
                    data[key] = [element]
                else:
                    data[key].append(element)
    return data

def check_cmd_argv(argv):
    len_argv = len(argv)
    if len_argv <= 1:
        sys.exit("Too few command-line arguments")
    elif len_argv > 2:
        sys.exit("Too many command-line arguments")
    elif len_argv == 2:
        input_file = argv[1]
        if Path(input_file).suffix != ".csv":
            sys.exit("Not a CSV file")
        elif input_file not in os.listdir("."):
            sys.exit("File does not exist")
        else:
            return input_file

if __name__ == "__main__":
    main()