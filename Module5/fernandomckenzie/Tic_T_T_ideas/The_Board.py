
#print board
The_Board = {'top-L0':'o','top-M1':'x','top-R2':'0',
             'mid-L3':'x','mid-M4':'_','mid-R5':'x',
             'low-L6':'x','low-M7':'x','low-R8':'0',}
def printBoard(board):
  print(board['top-L0'] +'|'+ board['top-M1'] +'|'+ board['top-R2']) 
  print('-+-+-')
  print(board['mid-L3'] +'|'+ board['mid-M4'] +'|'+ board['mid-R5'])
  print('-+-+-') 
  print(board['low-L6'] +'|'+ board['low-M7'] +'|'+ board['low-R8']) 
print(The_Board)
#________________
# eval position 
X_P1 = 'X'
O_P2 = 'O'
blank_space = '_'
# _______________
X_Wins = 'X Wins!'
O_Wins = 'O Wins!'
DRAW = 'Draw!'
#________________

#if statement check line1
#print(board['top-L0'] +'|'+ board['top-M1'] +'|'+ board['top-R2']) 
#true

#if statement check line2
#print(board['mid-L3'] +'|'+ board['mid-M4'] +'|'+ board['mid-R5']).
#True

#if statement check line3
#print(board['low-L6'] +'|'+ board['low-M7'] +'|'+ board['low-R8'])  
#true

#if statement check line4
#print(board['top-L0'] +'|'+ board['top-M3'] +'|'+ board['top-R6']) 

#check line5
#print(board['mid-L1'] +'|'+ board['mid-M4'] +'|'+ board['mid-R7']) 

#if statement check line6
#print(board['low-L2'] +'|'+ board['low-M5'] +'|'+ board['low-R8']) 


# if statement check cross line7
#print(board['top-L0'] +'|'+ board['mid-M4'] +'|'+ board['low-R8']) 

#if statement check cross line8
#print(board['top-R2'] +'|'+ board['mid-M4'] +'|'+ board['low-L6']) 

#if statement  check middle line9
#print(board['top-m1'] +'|'+ board['mid-M4'] +'|'+ board['low-m7']) 

#if boardfull(The-Board):
    #print('tie!!')
# if checkAll('X') == True:        do the same for ('O')
# print(x wins)
# break;


