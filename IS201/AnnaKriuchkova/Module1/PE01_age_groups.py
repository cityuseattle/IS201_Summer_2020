#IS201_Summer_2020 Module 1 PE01
#Anna Kriuchkova

#Set a variable 'age'. Prompt the user to enter one's age. 
age = input ("Welcome! Please enter your age: ")
#Display input back to user
print ("\nYou are " + age + " years old.")
#Make sure the input value is converted to a numerical representation (int)
age = int(age)

#Set an age_group value that will store user's stage of life
age_group = " "

#Using if-elif-else chain, determine user's stage of life, based on age input
if age < 2:
    age_group = "a baby."
elif age < 4:
    age_group = "a toddler."
elif age < 13:
    age_group = "a kid."
elif age < 20:
    age_group = "a teenager."
elif age < 65:
    age_group = "an adult."
else:
    age_group = "an elder."

#Set a message that will show the user a result
message = "\nYou are " + age_group
#Print the message
print (message) 
