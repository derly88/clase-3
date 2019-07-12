from punto import *
from math import pi

class Figura:
    def __init__(self,p1,p2):
        self.origen=p1
        self.fin=p2

class Cuadrado(Figura):

    def __init__(self,p1,p2):
        self.origen=p1
        self.fin=p2
        self.lado=self.origen.calcular_dist(self.fin)
    def calcular_area(self):
        
        self.area=self.lado*self.lado
    def calcular_perimetro(self):
        
        self.perimetro=4*self.lado
            
class Circulo(Figura):
    def calcular_area(self):
        radio=self.origen.calcular_dist(self.fin)
        self.area=pi*(radio**2)
    def calcular_perimetro(self):
        radio=self.origen.calcular_dist(self.fin)
        self.perimetro=2*pi*radio

class Triangulo(Figura):
    def calcular_area (self):
        p=punto(self.origen.x,self.fin.y)
        base=self.origen.calcular_dist(p)
        altura=self.fin.calcular_dist(p)
        self.area=(base*altura)/2
    def calcular_perimetro(self):
        p=punto(self.origen.x,self.fin.y)
        base=self.origen.calcular_dist(p)
        altura=self.fin.calcular_dist(p)
        hipo=self.origen.calcular_dist(self.fin)
        self.perimetro=base+hipo+altura
        
        
