from math import sqrt

class punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def calcular_dist(self,punto):
        distancia=sqrt((self.x-punto.x)**2+(self.y-punto.y)**2)
        return distancia
