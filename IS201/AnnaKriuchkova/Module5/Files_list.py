filename = 'C:\\Users\\AnnaK\\IS201_Summer_2020\\IS201\\AnnaKriuchkova\\Module5\\hello.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines: 
    print(line.rstrip())
    