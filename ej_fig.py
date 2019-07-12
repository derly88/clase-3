from fig import *

p1=punto(5,5)
p2=punto(5,10)
p3=punto(10,1)
cuadrado=Cuadrado(p1,p2)
circulo=Circulo(p1,p2)
triangulo=Triangulo(p1,p3)

cuadrado.calcular_area()
circulo.calcular_area()
triangulo.calcular_area()
cuadrado.calcular_perimetro()
circulo.calcular_perimetro()
triangulo.calcular_perimetro()

print cuadrado.area
print circulo.area
print triangulo.area
print cuadrado.perimetro
print circulo.perimetro
print triangulo.perimetro

