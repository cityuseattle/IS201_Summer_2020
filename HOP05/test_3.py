try:
    fh = open("testfile","w")
    try:
        fh.write("test file exception handling!!")
        raise IOError 
    finally:
        print("Goin to close the file")
except IOError:
    print("Error: cant\'t find file or read data")
    fh.close()   
