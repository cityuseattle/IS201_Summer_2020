#define the file I will be working with and store its name in the variable 'guestlog'
guestlog = 'guestlog.txt'

#create a while loop that will allow to prompt for user input infinetely
while True: 
    guest = input("Please enter your name: ")
    #allow a user to exit the while loop\
    #if type 'quit'
    if guest == 'quit':
        break 
    #append to guestlog every time the user enters one's name
    with open(guestlog, 'a') as f:
        guestentry = f.write (str(guest) + " has accessed this file.\n")
        #display a message to the user 
        print("Hi, " + str(guest) + "! Your visit has been logged.")

