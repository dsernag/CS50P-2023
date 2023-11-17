import pathlib

def main(user_input):
    str_user_input = user_input.strip().lower()
    extension = pathlib.Path(str_user_input).suffix
    if extension in file_dict_mime.keys():
        print(f"{file_dict_mime.get(extension)}")
    else:
        print("application/octet-stream")

#
if __name__ == "__main__":
    file_dict_mime = {
        ".gif" : "image/gif" ,
        ".jpg" : "image/jpeg" ,
        ".jpeg" : "image/jpeg" ,
        ".png" : "image/png" ,
        ".pdf" : "application/pdf" ,
        ".txt" : "text/plain" ,
        ".zip" : "application/zip"}
    user_input = input("File name: ")
    main(user_input)

