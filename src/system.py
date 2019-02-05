class Matrix:
    """
    Class for 3x3 matrices.
    """
    def __init__(self, A1, A2, A3, B1, B2, B3, C1, C2, C3):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.B1 = B1
        self.B2 = B2
        self.B3 = B3
        self.C1 = C1
        self.C2 = C2
        self.C3 = C3

    def sarrus(self):
        """
        Sarrus' rule for 3x3 matrices' determinant.
        """
        first = (self.A1 * self.B2 * self.C3)
        second = (self.B1 * self.C2 * self.A3)
        third = (self.C1 * self.A2 * self.B3)
        fourth = (self.C1 * self.B2 * self.A3)
        fifth = (self.B1 * self.A2 * self.C3)
        sixth = (self.A1 * self.C2 * self.B3)
        return first + second + third - fourth - fifth - sixth

class System:
    """
    Class for linear systems of equations in three variables (3x3 system).
    This class solves the system with Cramer's rule.
    Equations form: ax + by + cz = d
    """
    def __init__(self, a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

    def __determinant(self):
        """
        Calculates the determinant of the first matrix.
        """
        Dmatrix = Matrix(self.a1, self.a2, self.a3, self.b1, self.b2, self.b3, self.c1, self.c2, self.c3)
        self.D = Dmatrix.sarrus()
    
    def __determinantX(self):
        """
        Calculates the determinant of the second matrix.
        """
        DXmatrix = Matrix(self.d1, self.d2, self.d3, self.b1, self.b2, self.b3, self.c1, self.c2, self.c3)
        self.DX = DXmatrix.sarrus()
    
    def __determinantY(self):
        """
        Calculates the determinant of the third matrix.
        """
        DYmatrix = Matrix(self.a1, self.a2, self.a3, self.d1, self.d2, self.d3, self.c1, self.c2, self.c3)
        self.DY = DYmatrix.sarrus()
    
    def __determinantZ(self):
        """
        Calculates the determinant of the fourth matrix.
        """
        DZmatrix = Matrix(self.a1, self.a2, self.a3, self.b1, self.b2, self.b3, self.d1, self.d2, self.d3)
        self.DZ = DZmatrix.sarrus()
    
    def solve(self):
        """
        Returns the results of the three variables.
        """
        self.__determinant()
        self.__determinantX()
        self.__determinantY()
        self.__determinantZ()
        return self.DX / self.D, self.DY / self.D, self.DZ / self.D

def main():
    print("Format: ax + by + cz = d")
    
    Acoeff = input("Enter A coefficients as CSV (a1,a2,a3): ")
    Bcoeff = input("Enter B coefficients as CSV (b1,b2,b3): ")
    Ccoeff = input("Enter C coefficients as CSV (c1,c2,c3): ")
    Dcoeff = input("Enter D coefficients as CSV (d1,d2,d3): ")

    A = list(map(float, Acoeff.split(",")))
    B = list(map(float, Bcoeff.split(",")))
    C = list(map(float, Ccoeff.split(",")))
    D = list(map(float, Dcoeff.split(",")))

    system = System(A[0], A[1], A[2], B[0], B[1], B[2], C[0], C[1], C[2], D[0], D[1], D[2])

    print(system.solve())

if __name__ == "__main__":
    main()
