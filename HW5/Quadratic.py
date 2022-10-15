from math import sqrt
class Quadratic():
    def __init__(self,a: int = 0 ,b: int = 0 ,c: int = 0) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def __repr__(self) -> str:
        return """
        Quadratic({},{},{})
        """.format(self.a,self.b,self.c)

    def __str__(self) -> str:
        return ("""
        A: {}
        B:{}
        C:{}
        Discriminant: {}
        Roots: {}""".format(self.a,self.b,self.c,self.discriminant(),self.roots()))

    def discriminant(self):
        return (self.b**2)-4*self.a*self.c

    def roots(self):
        roots = []
        try: 
            mainRoot = sqrt(self.discriminant())
            roots.append((-self.b + mainRoot)/(2*self.a))
            roots.append((-self.b - mainRoot)/(2*self.a))
            return roots
        except ValueError:
            return "No real roots"

if __name__ == "__main__":
    # We create the objects to test them
    q1 = Quadratic(1,-4,3)# Expected roots are 3 and 1
    q2 = Quadratic(1,3,-10)# Expected roots are 2 and -5
    q3 = Quadratic(4,12,9)# Expected root is only -3/2. So both roots should be the same
    q4 = Quadratic(2,4,8)# Expected imaginary roots
    # We print the representation of the objects
    print(repr(q1))
    print(repr(q2))
    print(repr(q3))
    print(repr(q4))

    # We print the string representation of the objects
    print(q1)
    print(q2)
    print(q3)
    print(q4)

    # We assert the correct roots of the objects

    # Assert for Q1
    assert(q1.roots()[0] == 3.0)
    assert(q1.roots()[1] == 1.0)
    # Assert for Q2 
    assert(q2.roots()[0] == 2.0)
    assert(q2.roots()[1] == -5.0)
    # Assert for Q3
    assert(q3.roots()[0] == -1.5)
    assert(q3.roots()[1] == -1.5)
    # Assert for Q4   
    assert(q4.roots() == "No real roots")

    # For the import part of the exercise, I imported it directly in the python console, and it worked. 