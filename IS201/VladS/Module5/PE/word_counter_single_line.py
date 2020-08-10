#This program counts words in a text file by counting intervals between words as well as new lines. It assumes the text file is correctly formatted (i.e. absence of empty intervals at the end of lines, double intervals between words, or intervals before punctuation signs).

#initializing the counter
count=0
#opening the data.txt file to read
with open('data.txt') as source_file:
  
#reading one char at a time and checking if it matches an interval (word delimiter) or new line (it would not have an interval before the first word) and adding to the counter
  while 1:
   char = source_file.read(1)
   if char == " " or char == "\n":
    count += 1
   elif not char:
        break
#the number of words will be the number of intervals + 1 (i.e. one interval between each two words). This prints the number of words in the text file.
  print("This file has:",count+1,"words.")


