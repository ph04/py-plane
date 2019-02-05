from math import sqrt
import system

class Triangle:
    def __init__(self, xA, xB, xC, yA, yB, yC):
        self.xA = xA
        self.xB = xB
        self.xC = xC
        self.yA = yA
        self.yB = yB
        self.yC = yC

    def orthocenter(self):
        """
        Returns orthocenter's coordinates.
        """
        xO = (((self.xA*(self.xC-self.xB)/(self.yC-self.yB))+self.yA-(self.xB*(self.xC-self.xA)/(self.yC-self.yA))-self.yB)*(((self.yC-self.yA)*(self.yC-self.yB))/((self.xC-self.xA)*(self.xC-self.xB))))/(((self.yC-self.yA)/(self.xC-self.xA))-((self.yC-self.yB)/(self.xC-self.xB)))
        yO = (xO*(self.xA-self.xC)/(self.yC-self.yA))+(self.xB*(self.xC-self.xA)/(self.yC-self.yA))+self.yB
        return xO, yO

    def circumcenter(self):
        """
        Returns circumcenter's coordinates.
        """
        xP = (((self.xA+self.xB)/2)*((self.xA-self.xB)/(self.yB-self.yA))-((self.xB+self.xC)/2)*((self.xC-self.xB)/(self.yB-self.yC))+((self.yB+self.yC)/2)-((self.yA+self.yB)/2))/(((self.xA-self.xB)/(self.yB-self.yA))-((self.xC-self.xB)/(self.yB-self.yC)))
        yP = ((self.xB-self.xC)*(self.xB+self.xC)+(self.yB+self.yC)*(self.yB-self.yC)-2*(self.xB-self.xC)*xP)/(2*(self.yB-self.yC))
        return xP, yP

    def area(self):
        """
        Returns area's value.
        """
        matrix = system.Matrix(1, 1, 1, self.xA, self.xB, self.xC, self.yA, self.yB, self.yC).sarrus()
        return 0.5 * abs(matrix)

    def barycenter(self):
        """
        Returns barycenter's coordinates.
        """
        return (self.xA + self.xB + self.xC) / 3, (self.yA + self.yB + self.yC) / 3

class Parabola:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def vertex(self):
        """
        Returns vertex's coordinates.
        """
        return -self.b / (2 * self.a), (4 * self.a * self.c - self.b**2) / (4 * self.a)

    def focus(self):
        """
        Returns focus' coordinates.
        """
        return -self.b / (2 * self.a), (1 - (self.b**2 - 4 * self.a * self.c)) / (4 * self.a)
    
    def axis(self):
        """
        Returns axis' equation.
        """
        return -self.b / (2 * self.a)

class Circumference:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def center(self):
        """
        Returns center's coordinates.
        """
        return (-self.a / 2, -self.b / 2)

    def radius(self):
        """
        Returns radius' length.
        """
        return 0.5 * sqrt((self.a**2) + (self.b**2) - (4 * self.c))

def triangle():
    xa = float(input("Enter xA: "))
    xb = float(input("Enter xB: "))
    xc = float(input("Enter xC: "))
    ya = float(input("Enter yA: "))
    yb = float(input("Enter yB: "))
    yc = float(input("Enter yC: "))

    triang = Triangle(xa, xb, xc, ya, yb, yc)

    print(f"Area is {triang.area()}")
    print(f"Circumcenter is {triang.circumcenter()}")
    print(f"Barycenter is {triang.barycenter()}")
    print(f"Orthocenter is {triang.orthocenter()}")

def parabola():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    parab = Parabola(a, b, c)

    print(f"Vertex is {parab.vertex()}")
    print(f"Focus is {parab.focus()}")
    print(f"Axis is x = {parab.axis()}")

def circumference():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    circ = Circumference(a, b, c)

    print(f"Center is {circ.center()}")
    print(f"Radius is {circ.radius()}")

def main():
    print("Choose your graph: ")
    print("1) Triangle")
    print("2) Parabola")
    print("3) Circumference")
    
    choice = input()

    if choice == "1":
        triangle()
    elif choice == "2":
        parabola()
    elif choice == "3":
        circumference()
    else:
        raise ValueError("Invalid choice.")

if __name__ == "__main__":
    main()
