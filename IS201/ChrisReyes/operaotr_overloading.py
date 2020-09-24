class Point:
    def _init_(self, x, y):
        self.x = x
        self.y = y
    #overriding magic
    def _add_(self, other):
        return self.x + other.x, self.y + other.y
p1 = Point(1,2)
p2 = Point(3, 4)

orint(p1+p2)
    