try:
    fh = open("testfile","r")
    fh.write("This is my test file for exception handlign!!")
except IOError:
    print("Error: can\'t find file or read data")
finally:
    print("Going to close the file")
    fh.close()
   