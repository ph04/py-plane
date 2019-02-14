from math import sqrt

class LinearEquation:
    """
    Class for Linear Equations.
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
        if not self.a:
            raise ValueError("A parameter can't be 0, the equation does not exist.")

    def solve(self):
        """
        Returns the result for the given equation.
        """
        return -self.b / self.a
    
    def form(self, param = 'x'):
        """
        Returns the given equation with the given parameter ('x' is set by default).
        """
        if len(param) > 1:
            raise ValueError("Invalid parameter length.")
        return str(self.a) + param + " + " + str(self.b) + " = 0"

class SecondGradeEquation:
    """
    Class for Second Grade Equations.
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.a:
            raise ValueError("'a' parameter can't be 0, the equation does not exist.")
    
    def solve(self):
        """
        Returns the results for the given equation.
        """
        root = sqrt((self.b**2) - (4 * self.a * self.c))
        return (-self.b + root) / (2 * self.a), (-self.b - root) / (2 * self.a)
    
    def form(self, param = 'x'):
        """
        Returns the given equation with the given parameter ('x' is set by default).
        """
        if len(param) > 1:
            raise ValueError("Invalid parameter length.")
        return str(self.a) + param + "^2 + " + str(self.b) + param +" + " + str(self.c) + " = 0"

def main():
    """
    Example of usage.
    """
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    eq1 = LinearEquation(a, b)
    eq2 = SecondGradeEquation(a, b, c)

    print(f"The result of {eq1.form('k')} is {eq1.solve()}")
    print(f"The result of {eq2.form()} is {eq2.solve()}")

if __name__ == "__main__":
    main()
