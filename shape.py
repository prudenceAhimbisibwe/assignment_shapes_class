import math
class Circle:
    # finding area of a circle
    def __init__(self,r):
        self.r=r

    def area(self):
        A=math.pi*self.r**2
        return A
    # finding circumference of a circle
    def circumference(self):
        C=2*(math.pi*self.r)
        return C

class Square:
    # Calculating the area of a square
    def __init__(self,a):
        self.a=a
    def area(self):
        A=self.a**2
        return A
    # calculating the perimeter of a square
    def perimeter(self):
        P=4*self.a
        return P

class Rectangle:
    # Calculating the area of a rectangle
     def __init__(self,w,l):
         self.w=w
         self.l=l
     def area(self):
         A=self.w*self.l
         return A
    # calculating the perimeter of a rectangle
     def perimeter(self):
         P=2*(self.w+self.l)
         return P

class Sphere:
    # calculating the area of a sphere 
    def __init__(self,r):
        self.r=r

    def surface_area(self):
        S=4*(math.pi*self.r**2)
        return S
    # calculating the volume of a sphere
    def volume(self):
        V=4/3*(math.pi*self.r**3)
        return V
    




    