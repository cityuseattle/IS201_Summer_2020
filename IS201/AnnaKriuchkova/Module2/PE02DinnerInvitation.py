#IS201_Summer_2020
#PE02 Lists and Tuples
#AnnaKriuchkova


#create an initial list of invitees; display it to the user
invitees = ['Jasmine', 'Karen', 'Ali']
print(invitees)

#replace an attendee at index 1 
invitees[1] = 'Emma'
print(invitees)

#insert a guest at the beginning of the list
invitees.insert(0, 'Lisa')
#insert a guest at the middle of the list
invitees.insert(3, 'Vita')
#append a guest at the end of the list
invitees.append('Raymond')
#display new list to the user
print(invitees)

#remove guests, using pop() method; 
#display messages for removed guests
print('Sorry, ' + invitees.pop() + ', I cannot invite you to dinner')
print('Sorry, ' + invitees.pop(0) + ', I cannot invite you to dinner')
print('Sorry, ' + invitees.pop(-1) + ', I cannot invite you to dinner')
print('Sorry, ' + invitees.pop(-3) + ', I cannot invite you to dinner')

#display final list of attendees;
#items from the list are displayed one at a time to ensure neat formatting
print('Guests, invited to dinner:', invitees[0] + ' and ' + invitees[1])
