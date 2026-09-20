class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.scores = []

    def add_score(self, score):
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be numeric")

        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")

        self.scores.append(score)


class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


def letter_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be numeric")

    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


class Roster:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        score_count = len(student.scores)

        if score_count < 1 or score_count > 6:
            raise ValueError("Student must have between 1 and 6 scores")

        self.students.append(student)


def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")

    if name == "":
        raise ValueError("Name cannot be empty")

    if len(name) > 50:
        raise ValueError("Name cannot exceed 50 characters")

    for character in name:
        if not (character.isalpha() or character == " " or character == "-"):
            raise ValueError("Name can contain only letters, spaces, and hyphens")

    return True


