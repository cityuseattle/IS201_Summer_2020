#IS201 Module 4 PE04 Functions
#AnnaKriuchkova

#Exercise 1

#define a make_shirt() function, with size and text as its parameters
def make_shirt(size, text):
    """Create a function that will automate the T-shirt order process"""
    #summarize the order and display it to the user
    print(f"You have ordered the {size} size T-shirt. Selected logo is {text}.")

#call the function, using positional arguments
make_shirt("S", "Positive vibes")
#call the function, using keyword arguments
make_shirt(size="M", text="CityU TECH")

#Exercise 2

#modify a make_shirt() function to include default parameters
def make_shirt(size="L", text="I love Python"):
    """Create a function that will automate the T-shirt order process"""
    #summarize the order and display it to the user
    print(f"You have ordered the {size} size T-shirt. Selected logo is {text}.") 

#call the function, using default parameters
make_shirt()
#call the function with changing default parameter for size to a customized one
make_shirt(size="M")
#call the function with changing both default parameters to customized ones
make_shirt("S", "Ghibli Studio")

#Extra practice

#define make_shirt function, with size and message as its parameters
def make_shirt(size, message):
    """Generate T-shirt order, based on user input"""
    #ask a user to enter T-shirt size
    size = input("Please enter your size. Available sizes are: S,M,L - ")
    #define selection of sizes, using a list
    sizes = ['S','M','L', 's', 'm', 'l']

#eliminate sizes, that are not in the list, by using while loop, along with not in method 
#make sure user gets to enter a size again
               
    while size not in sizes: 
        print("Sorry, this size is currently unavailable")
        size = input("Please try again. Available sizes are: S, M, L - ")
        
#ask a user to enter text for T-shirt logo
    message = input("Please enter a logo for your T-shirt: ")
#handle instances when users don't want any logo
    if len(message) == 0:
        print("Are you sure you don't want any logo?")
        response = input("Type 'Y' to continue or 'N' to try again: ")
        if response == 'Y':
            print(f"Your order is processed. Selected size: {size}. No logo is chosen.")
            exit()
        elif response == 'N':
            make_shirt(size, message)
        else:
            exit()

#display final order to the user
    print(f"Your order is processed. Selected size: {size}. Selected logo: {message}.")
    exit()

#call in make_shirt function
make_shirt(size = input, message = input)