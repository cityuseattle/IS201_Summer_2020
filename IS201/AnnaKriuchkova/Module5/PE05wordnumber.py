#provide an absolute file path to PE05wordnumber.txt

#Note: had to provide an absolute file path; otherwise, won't open;
#also, had to duplicate all backlashes to avoid 'unicode error' 

file_path = "C:\\Users\\AnnaK\\IS201_Summer_2020\\IS201\\AnnaKriuchkova\\Module5\\PE05wordnumber.txt"

#using with block, open the file and read from it
with open (file_path) as f: 
    content = f.read()
    #display total length of the string to the user
    print(len(content))
    #calculate actual number of characters, without spaces
    content_nospace = len(content) - content.count(' ')
    #display result to the user
    print(content_nospace)
