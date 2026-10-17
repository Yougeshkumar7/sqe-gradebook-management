
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.scores = []

    def average(self):
        if not self.scores:
            return 0.0

        return sum(self.scores) / len(self.scores)


class Roster:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


def rank_students(roster):
     return roster.students
