for num in range(1-, 20):    #to iterate between 10 to 20 
    for i in range(2, num): #to iterate on the factor of the number
        if num%i == 0:      # to determine the first factor 
            j=num/i         # to calculate the second factor 
            print ('%d equaals %d * %d' % (num,i,j))
            break           # to move to the next number , the #first For
  else:                     # else part of the loop
      print ( num,'is a prime number')