alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'colot': 'yellow','points': 10}

aliens =[alien_0,alien_1]

#Accessing key, Value
for i in aliens:
    for key,value in i.items():
        print("KEY:", key,"\t", "VALUE :", value)
        