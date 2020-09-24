alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'Yellow', 'points': 10}

aliens = [alien_0,alien_1]

#Accessing key,value

for i in aliens:
    for key, value in i.items():
        print("Key:", key, "\t" , "VALUE :", value)