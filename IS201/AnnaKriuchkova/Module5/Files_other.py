file_path = "C:\\Users\\AnnaK\\IS201_Summer_2020\\IS201\\AnnaKriuchkova\\Module5\\hello.txt"

with open(file_path) as file_object:
    contents = file_object.read()
print(contents)