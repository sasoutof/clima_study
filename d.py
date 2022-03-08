import math
class Point:
    def __init__(self, initX, initY ):
        self.x = initX
        self.y = initY
        def getX(self):return self.x
        def getY(self):return self.y
        def distanciaDOrigen(self):
            return math.sqrt((self.x ** 2) + (self.y ** 2))
        def distancia(self, point2):
            xdiff = point2.getX()-self.getX()
            ydiff = point2.getY()-self.getY()
            dist = math.sqrt(xdiff**2 + ydiff**2)
            return dist
p = Point(7,6)
q = Point(4,3)
print(p.distancia(q))