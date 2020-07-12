#IS201_Summer_2020 Module 1 PE01
#Anna Kriuchkova

#Prompt user to enter a number
number = input("Hi! Please enter a number: ")
#Make sure the input value is converted to a numerical representation
number = int(number)
#Check, whether entered value is a prime number, by using for-loop.
#Note: a prime number is a whole number > 1;
#prime number can be divided only by itself or by 1 without a remainder. 

if number > 1:
#Check if the number has factors other than itself or 1; 
#if yes - it is not a prime number.
#use modulo (%) operator to determine, whether there is a remainder
#print a result to the user
    for i in range (2, number):
         if number %i == 0:
              print(number, "is not a prime number.")
              break
#make sure you use break statement; otherwise, the loop will keep running,
#until the number can only be divided by itself. 
    else:    
         print(number, "is a prime number.")
#if number is not greater than 1, it is not a prime number
else:
    print (number, "is not a prime number.")
