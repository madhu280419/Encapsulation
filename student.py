class Student:
    def __init__(self, roll, name, marks):
        self.rollNumber = roll
        self.name = name
        self.__marks = marks
        print("Student roll:", self.rollNumber, "Student name:", self.name)

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value >= 0:
            self.__marks = value
        else:
            print("Error: Marks can't be negative.")


student = Student(420, "mad", 75)
print("Student's marks:", student.marks)

#student.marks = -5 
student.marks = 95   
print("Updated marks:", student.marks)