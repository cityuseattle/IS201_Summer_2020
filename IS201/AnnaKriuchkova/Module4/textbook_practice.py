#passing information to a function
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('anna')
greet_user('sarah')

#Note : the argument 'anna' was passed to the function greet_user(), and the value was stored\
#in the parameter username

#Making an argument optional
def get_formatted_name(first_name, last_name, middle_name = " "):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#Returning a dictionary
def build_person(first_name, last_name, age=""):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person ['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

def greetPerson(*name):
    print('Hello', name)

greetPerson('David', 'Soloa')

def Foo(x):
    if (x==1):
        return 1
    else:
        return x+Foo(x-1)

print(Foo(4))

x = 50
def func():
    global x
    print('x is', x)
    x=2
    print('Changed global x to',x)
func()
print('Value of x is', x)
