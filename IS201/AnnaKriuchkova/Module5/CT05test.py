#define an absolute file path for conceptfile.txt
file_path = 'C:\\Users\\AnnaK\\IS201_Summer_2020\\IS201\\AnnaKriuchkova\\Module5\\conceptfile.txt'

with open (file_path, 'w') as file_object:
    file_object.write("Testing concepts for CT05, Module 5.\nLet's see what output I will get.")

#testing .read() method
with open (file_path) as file_object:
    conceptfile = file_object.read()
    print(conceptfile)

#testing .readline() method
with open (file_path) as file_object:
    concept_line = file_object.readline()
    print(concept_line, end="")
    
    concept_line = file_object.readline()
    print(concept_line)

#Output: Prints first line: Testing concepts for CT05, Module5. 
#Output: Prints next line: Let's see what output I will get. 

#testing .readlines() method
with open (file_path) as file_object:
    concept_lines = file_object.readlines()
    print(concept_lines)

#should be able to call the file content outside of 'with block'
print(concept_lines)

#testing .read(all)
#with open(file_path) as file_object:
    #concept_all = file_object.read(all)
    #print(concept_all)

try:
    1/0
except:
    print('exception') #executes, if there is an exception
else: 
    print('else') #executes, if no exception
finally:
    print('finally') #executes regardsless 

#Received output: 'exception' (because there is one) and 'finally' (because we prompted program to do so)





