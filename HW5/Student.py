from math import sqrt
from xmlrpc.client import Boolean
class Person():
    def __init__(self,name: str = "", lastName: str = "", age: int = 0, gender : Boolean = False, afiliation: str = "") -> None:# For the gender, we use False for Male and True for Female
        self.name = name
        self.lastName = lastName
        self.age = age
        self.gender = gender
        self.afiliation = afiliation
    
    def __repr__(self) -> str:
        return """
        Person({},{},{},{},{})
        """.format(self.name,self.lastName,self.age,self.gender,self.afiliation)

    def __str__(self) -> str:
        return ("""
        Name: {}
        Last Name:{}
        Age:{}
        Gender: {}
        Afiliation: {}""".format(self.name,self.lastName,self.age,self.gender, self.afiliation))
    
    def setName(self, newName: str = ""):#non-magic method. I could not think of many different methods for a person with basic attributes
        self.name = newName
    
    def isNameShort(self):
        totLen = len(self.name) + len(self.lastName)
        if totLen > 15:
            return "Long Name"
        return "Short Name"

class Student(Person):
    def __init__(self, name: str = "", lastName: str = "", age: int = 0, gender : Boolean = False, afiliation: str = "", major : str = "", gradesAverage: float = 0.0) -> None:
        super().__init__(name=name, lastName=lastName, age=age,gender=gender, afiliation=afiliation)
        self.major = major
        self.gradesAverage = gradesAverage
    
    def __repr__(self) -> str:
        return """
        Student({},{},{},{},{},{}, {})
        """.format(self.name,self.lastName,self.age,self.gender, self.afiliation, self.major, self.gradesAverage)

    def __str__(self) -> str:
        return ("""
        Name: {}
        Last Name:{}
        Age:{}
        Gender: {}
        Afiliation: {}
        Major: {}
        Average grades: {}""".format(self.name,self.lastName,self.age,self.gender, self.afiliation, self.major, self.gradesAverage))
    
    def setMajor(self, newMajor):
        self.major = newMajor

    def hasGoodGrades(self):
        if self.gradesAverage > 8.5:
            return "Good Grades"
        return "Bad Grades"

if __name__ == "__main__":
    P1 = Person("john", "smith", 21, False, "Canada")
    S1 = Student("john", "smith", 21, False, "University of Denver", "Data Science", 8.5)
    print(P1)
    print(S1)

    #Check attributes
    assert(P1.name == "john")
    assert(P1.lastName == "smith")
    assert(P1.age == 21)
    assert(P1.gender == False)
    assert(P1.afiliation == "Canada")

    assert(S1.major == "Data Science")
    assert(S1.gradesAverage == 8.5)
    # Return methods
    assert(P1.isNameShort() == "Short Name")

    assert(S1.hasGoodGrades() == "Bad Grades")
    # For the import part of the exercise, I imported it directly in the python console, and it worked. 