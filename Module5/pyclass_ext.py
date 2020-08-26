def uppering (inL):
    for x in inL:
        if(x[0].isupper()== True):
            print(x)

L = ["This", "is","the", "4th", "week"]
uppering(L)