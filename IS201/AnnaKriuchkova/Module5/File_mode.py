file_path = "C:\\Users\\AnnaK\\IS201_Summer_2020\\IS201\\AnnaKriuchkova\\Module5\\hello.txt"

file = open(file_path, 'a')
file.write('\nThis is a new content I just appended')
file.close()

new_file = open('world.txt', 'w')
new_file.write('This is a new file')
new_file.close()

file = open(file_path)
content = file.read()
file.close()
print(content) 