#Question #1: Correct answer is (3) 3 and 1
class A:
    print('Inside class')

A()  #object 1
A()  #object 2
obj = A() #obj is a reference variable, refers to object 3

#Question 2: Correct answer is (1) Class B inherits A, but the data field 'i' in A is not inherited.
class A:
    def __init__(self, i=0):
        self.i = i

class B(A):
    def __init__(self, j=0):
        self.j = j

def main():
    b = B()
    #print(b.i) #results in an AttributeError: 'B' object has no attribute 'i'
    print(b.j)
main()

#Output: Inside class 0

#Class B inherits A, however __init__() method is overwritten;\
#thus, instead of a default parameter i, class B has a default parameter j.

#You do not have to pass an argument to create a B object, unless you want to. 
#Class B already has a defined default parameter j=0 (pay attention to an output)
#As you can see above, data field j can be accessed by object b. 
