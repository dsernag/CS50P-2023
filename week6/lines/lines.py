import sys
from pathlib import Path
import os

def main():
    args = sys.argv
    input_file = check_cmd_args(args)
    complexity = openfile_countlines(input_file)
    print(complexity)

def openfile_countlines(input_path):
    lines = 0
    with open(input_path, 'r') as file:
        for row in file.readlines():
            if validate_row(row):
                lines += 1
            else:
                continue
    return lines

# Extracted from: https://www.youtube.com/watch?v=NEd3-fFs0zE
def validate_row(row):
    if row.isspace():
        return False
    elif row.lstrip().startswith('#'):
        return False
    else:
        return True


def check_cmd_args(args):
    len_args = len(args)
    if len_args <= 1:
        sys.exit("Too few command-line arguments")
    elif len_args > 2:
        sys.exit("Too many command-line arguments")
    elif len_args == 2:
        input_file = args[1]
        if Path(input_file).suffix != ".py":
            sys.exit("Not a Python file")
        elif input_file not in os.listdir("."):
            sys.exit("File does not exist")
        else:
            return input_file

if __name__ == "__main__":
    main()