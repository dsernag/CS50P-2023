import csv
import sys
import os
from pathlib import Path

def main():
    input_file, output_file = check_cmd_argv(sys.argv)
    list_data = obtain_data(input_file)
    write_data(list_data, output_file)

def write_data(list_data, output_file):
    with open(output_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        for record in list_data:
            writer.writerow(transform_record(record))

def transform_record(record):
    new_record = {}
    new_record["first"] = record["name"].split(",")[1].strip()
    new_record["last"] = record["name"].split(",")[0].strip()
    new_record["house"] = record["house"].strip()
    return new_record

def obtain_data(input_path):
    data = []
    with open(input_path, 'r') as file:
        for row in csv.DictReader(file):
                data.append(row)
    return data

def check_cmd_argv(argv):
    len_argv = len(argv)
    if len_argv < 3:
        sys.exit("Too few command-line arguments")
    elif len_argv > 3:
        sys.exit("Too many command-line arguments")
    elif len_argv == 3:
        input_file = argv[1]
        output_file = argv[2]
        if Path(input_file).suffix != ".csv" or Path(output_file).suffix != ".csv":
            sys.exit("Not a CSV file")
        elif input_file not in os.listdir("."):
            sys.exit(f"Could not read {input_file}")
        else:
            return [input_file, output_file]

if __name__ == "__main__":
    main()