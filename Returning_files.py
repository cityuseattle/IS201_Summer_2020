try:
    f= open('guest_book.txt', 'w')
    print('Number of characters in a file')
    str = input()
    f.write(str)

finally:

    f.close()