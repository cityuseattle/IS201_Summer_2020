file_path = 'C:\\Users\\AnnaK\\IS201_Summer_2020\\IS201\\AnnaKriuchkova\\Module5\\pi_digits.txt'
with open(file_path) as file_object:
    contents  = file_object.read()
    print(contents)

#for file_path can also prefix with r 

with open(file_path) as file_object:
    for line in file_object:
        print(line)

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

filename = "programming.txt"
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

filename = 'numbers.json'
with open (filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)