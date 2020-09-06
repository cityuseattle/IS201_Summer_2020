print('This program will um of numbers from 1 to a number you enter.')
print('please enter a ending number: ')
num = int(input())
total = 0 

while num >= 1:
    total += num
    num -= 1
print('The sum is: ' +str(total))
