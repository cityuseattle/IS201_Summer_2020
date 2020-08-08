#Note: had to provide an absolute file path; otherwise, won't open;
#also, had to duplicate all backlashes to avoid 'unicode error'

file_path = "C:\\Users\\AnnaK\\IS201_Summer_2020\\IS201\\AnnaKriuchkova\\Module5\\hello.txt"

file = open(file_path)
print(file.read())

