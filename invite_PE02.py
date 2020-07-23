Guests = ['Jalen', 'Ziante', 'Laylani']
print(Guests)

#del
Guests = ['Jalen', 'Ziante', 'Laylani']
del Guests[0]
print(Guests)

#insert
Guests.insert(0, 'Tom')
print("New Guest List: ",Guests)

#insert
Guests.insert(1, 'Jeff')
print(Guests)

#insert
Guests.insert(3, 'Buck')
print(Guests)

#append
Guests.append('John')
print("Another Guest List: ",Guests)

#pop
Guests = ['Tom', 'Jeff', 'Ziante', 'Buck', 'Laylani', 'John']
popped_Guest = Guests.pop(0)
print(Guests)
print(popped_Guest)
print("I apologize that you cannot make it.")

#pop
Guests = ['Jeff', 'Ziante', 'Buck', 'Laylani', 'John']
popped_Guest = Guests.pop(2)
print(Guests)
print(popped_Guest)
print("I apologize that you cannot make it.")

#pop
Guests = ['Jeff', 'Ziante', 'Laylani', 'John']
popped_Guest = Guests.pop(-1)
print(Guests)
print(popped_Guest)
print("I apologize that you cannot make it.")

#pop
Guests = ['Jeff', 'Ziante', 'Laylani']
popped_Guest = Guests.pop(2)
print(Guests)
print(popped_Guest)
print("I apologize that you cannot make it.")