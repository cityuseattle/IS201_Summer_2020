#IS201_Summer_2020
#PE02 Lists and Tuples
#AnnaKriuchkova


#create a list of animals
animals = ['lion', 'badger', 'otter', 'llama', 'bear', 'ocelot', 'elephant', 
'giraffe', 'hedgehog']

#use range(len(animals)), along with for loop,\
#to iterate over the indexes of the list and \
#print each animal to the user

for i in range (len(animals)): 
    print("Animal ", str(i), ' is: ', animals[i])

#slice first three items from the list;
#display them to the user
print("The first three items in the list are:", animals[:3])

#slice second three items from the list;
#display them to the user
print("Three items from the middle of the list are:", animals[3:6])

#slice last three items from the list;
#display them to the user
print("The last three items in the list are: ", animals[6:])

