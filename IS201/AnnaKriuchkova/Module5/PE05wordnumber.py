#provide an absolute file path to PE05wordnumber.txt

#Note: had to provide an absolute file path; otherwise, won't open;
#also, had to duplicate all backlashes to avoid 'unicode error' 

file_path = "C:\\Users\\AnnaK\\IS201_Summer_2020\\IS201\\AnnaKriuchkova\\Module5\\PE05wordnumber.txt"

#using with block, open a file and read from it
with open(file_path) as f:
    content = f.read()
    #calculate a total number of words in a text file
    print("Total number of words in a file is: ", len(content.split()))
    #calculate a total number of characters in a text file (excluding spaces);
    #display a result to the user
    character_count = len(content) - content.count(' ') 
    print("Total number of characters in a file (excluding spaces) is: ", character_count)