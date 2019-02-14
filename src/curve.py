import system

class Curve:
    """
    Class for parabolas and circumferences.
    """
    def __init__(self, xA, yA, xB, yB, xC, yC):
        self.xA = xA
        self.yA = yA
        self.xB = xB
        self.yB = yB
        self.xC = xC
        self.yC = yC
    
    def parabola(self):
        """
        Returns the defined parabola by A, B and C.
        """
        a1 = self.xA**2
        a2 = self.xB**2
        a3 = self.xC**2
        self.parabsystem = system.System(a1, a2, a3, self.xA, self.xB, self.xC, 1, 1, 1, self.yA, self.yB, self.yC)
        return self.parabsystem.solve()
    
    def circumference(self):
        """
        Returns the defined circumference by A, B and C.
        """
        d1 = -self.xA**2 - self.yA**2
        d2 = -self.xB**2 - self.yB**2
        d3 = -self.xC**2 - self.yC**2
        self.circsystem = system.System(self.xA, self.xB, self.xC, self.yA, self.yB, self.yC, 1, 1, 1, d1, d2, d3)
        return self.circsystem.solve()

def main():
    Acoord = input("Enter A coordinates as CSV (xA, yA): ")
    Bcoord = input("Enter B coordinates as CSV (xB, yB): ")
    Ccoord = input("Enter C coordinates as CSV (xC, yC): ")

    A = list(map(float, Acoord.split(",")))
    B = list(map(float, Bcoord.split(",")))
    C = list(map(float, Ccoord.split(",")))

    curve = Curve(A[0], A[1], B[0], B[1], C[0], C[1])
    
    print(f"A, B and C values for the defined circumference are {curve.circumference()}")
    print(f"A, B and C values for the defined parabola are {curve.parabola()}")

if __name__ == "__main__":
    main()
