class Parrot:
    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class penguin:

    def fly(self):
        print("penguin can't fly")

    def swim(self):
        print("penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = penguin()

#passing the object
flying_test(blu)
flying_test(peggy)
