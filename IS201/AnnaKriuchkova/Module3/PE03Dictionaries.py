#IS201 Module 3 PE03 Dictionaries and Sets
#Anna Kriuchkova

#Exercise #1

#define sample dictionaries
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

#using update() method, insert key-value pairs \
#from dict2 and dic3 into dic1

dic1.update(dic2)
dic1.update(dic3)

#display updated dic1 to the user
print(dic1)

#Exercise #2 

#Option 1

#define an empty dictionary 
doubled = {}

#set a range
#using for loop, determine key-value pairs (n:n*n)
for n in range(1,6):
    doubled[n] = n*n

#display a resulting dictionary to the user
print(doubled)

#Option 2: dictionary comprehension
#allows to minimize this task to one line of code

comprehend_doubled = {x: x*x for x in range (1,6)}
print(comprehend_doubled)
