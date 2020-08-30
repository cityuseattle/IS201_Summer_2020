name= input('Please enter your name ' )
filename = 'guest_book.txt'
with open(filename, 'w') as f:
    f.write(name)

try:
    f= open('guest_book.txt', 'w')
    print('Number of characters in a file')
    str = input()
    f.write(str)

finally:

    f.close()