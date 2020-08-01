#CT04 test
#Question 1

def  complex (real,imag):
    """Illustrate different ways of passing arguments"""
    print (str(real) + ' + ' + str(imag) +'j')

complex(3,4) #uses positional arguments, produces correct output
complex(3, imag=4) #uses a combination of positional and keyword arguments, produces correct output
complex(imag=4,real=3) #uses keyword arguments, produces correct output
#complex(real=3,4) #SyntaxError, positional argument needs to precede keyword argument;\
#however, if we trade them places - as in 'complex (4, real = 3)', we will end up with TypeError:\
#4 stands in the position of 'real' argument, so two values are being assigned to 'real' as a result

#Question 2

#*args is used to send a non-keyworded variable length argument list to the function

#**kwargs allows to pass keyworded variable length of arguments to a function

def myclassmates(*names_args):
    """Illustrate use of *args"""
    print(names_args)  #*args produces tuple in its output
    

myclassmates('Jalen', 'Christopher', 'Will', 'Nicolette', 'Vladimir', 'Fernando')

def myclassmates(**names_kwargs):
    """Illustrate use of **kwargs"""
    print(names_kwargs)

myclassmates(
    student1='Jalen', student2='Christopher', student3='Will', 
    student4='Nicolette', student5='Vladimir', student6='Fernando'
    ,) #*kwargs produces dictionary in the output

#deepcopy() function is used for copy by reference
#copy() function is used for copy by value or 'shallow' copy
