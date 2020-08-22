class Computer: 
    """This class is an example of encapsulation."""
    
    def __init__(self):
        self.__maxprice = 900 #this attribute is private! 

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice = price

c = Computer()
c.sell()

#change the price: notice that the output doesn't change!
c.__maxprice = 1000
c.sell()

#using setter function (takes price as a parameter)
c.setMaxPrice(1000)
c.sell()
