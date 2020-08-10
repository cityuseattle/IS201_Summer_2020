#opening guest_book.txt file for append access and checking if the user wants to add a name
with open('guest_book.txt','a') as log_file:
 while input("Do you want to enter a name? (y/n) ")=='y' or 'Y': 
#in case the user choses to add a name, prompts for a name, checks whether it's a number and prints a prompt to enter a string name
      name=input("Enter your name here: ")
      try:
       entry = float(name)
       print("Please, enter a string name!")
#in case the entry is not a number, prints the entered name and appends it to the file on a new line 
      except ValueError:
       print("Hello, ",name,"!")
       log_file.write(name)
       log_file.write("\n")
      break
    