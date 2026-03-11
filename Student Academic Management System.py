from datetime import date

class Student:
    def __init__(self, sid, name, m1, m2, m3, dob, fee_paid):
        self.sid = sid
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.dob = dob
        self.fee_paid = fee_paid
        self.total_fee = 50000

    def average_marks(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def calculate_cgpa(self):
        return self.average_marks() / 10

    def calculate_age(self):
        today = date.today()
        birth_year = int(self.dob.split("-")[0])
        return today.year - birth_year

    def fee_balance(self):
        return self.total_fee - self.fee_paid


class College:
    def __init__(self, code, name, location):
        self.code = code
        self.name = name
        self.location = location
        self.students = []

    def register_student(self, student):
        self.students.append(student)

    def display_details(self):
        print("College Code:", self.code)
        print("College Name:", self.name)
        print("Location:", self.location)

        for s in self.students:
            print("\nStudent ID:", s.sid)
            print("Name:", s.name)
            print("CGPA:", s.calculate_cgpa())
            print("Age:", s.calculate_age())
            print("Fee Balance:", s.fee_balance())


# Main Program
c = College("C101", "ABC College", "Vijayawada")

s1 = Student(1, "Rahul", 80, 85, 90, "2003-05-10", 30000)
s2 = Student(2, "Anita", 75, 88, 82, "2002-03-12", 35000)
s3 = Student(3, "Kiran", 70, 72, 68, "2004-07-15", 20000)

c.register_student(s1)
c.register_student(s2)
c.register_student(s3)

c.display_details()