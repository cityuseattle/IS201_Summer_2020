class Resturant:
    def __init__(self,name,food):
        self.name = name
        self.food = food

    def Describe_Resturant(self):
            return '{} {}'.format(self.name,self.food)
Rest_1 = Resturant('Casa Mia', 'Italian')

def Resturant_Open(self):
            return '{} {}'.format(self.name,self.food)
Rest_2 = Resturant('This resturant is open', 'If they sell Italian')

Rest_1.Describe_Resturant()
print(Resturant.Describe_Resturant(Rest_1))


Rest_2.Describe_Resturant()
print(Resturant.Describe_Resturant(Rest_2))


