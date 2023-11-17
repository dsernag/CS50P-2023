from PIL import Image, ImageOps
import sys
import os
from pathlib import Path

def main():
    input_path, output_path = check_cmd_argv(sys.argv)
    input_img = Image.open(input_path)
    shirt_img = Image.open("shirt.png")
    resized_img = ImageOps.fit(input_img, shirt_img.size)
    resized_img.paste(shirt_img, shirt_img)
    resized_img.save(output_path)

def check_cmd_argv(argv):
    len_argv = len(argv)
    if len_argv < 3:
        sys.exit("Too few command-line arguments")
    elif len_argv > 3:
        sys.exit("Too many command-line arguments")
    elif len_argv == 3:
        input_path = argv[1]
        output_path = argv[2]
        if Path(input_path).suffix.lower() not in [".jpg", ".jpeg", ".png"]\
            or Path(output_path).suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid input")
        elif Path(input_path).suffix.lower() != Path(output_path).suffix.lower():
            sys.exit("Input and output have different extensions")
        elif input_path not in os.listdir("."):
            sys.exit(f"Input does not exist")
        else:
            return input_path, output_path

if __name__ == "__main__":
    main()