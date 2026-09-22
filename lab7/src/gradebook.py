class Student:
    def __init__(self, name, roll_number):
        if not roll_number:
            raise ValueError("Student ID cannot be empty")

        if not isinstance(name, str):
            raise TypeError("Student name must be a string")

        if not name.strip():
            raise ValueError("Student name cannot be empty")

        self.name = name
        self.roll_number = roll_number
        self.scores = []

    def add_score(self, score):
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise TypeError("Score must be numeric")

        if score < 0:
            raise ValueError("Score cannot be negative")

        if score > 100:
            raise ValueError("Score cannot be greater than 100")

        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0.0

        return sum(self.scores) / len(self.scores)

    def grade_letter(self, score):
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise TypeError("Score must be numeric")

        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")

        if score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "F"


class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        for existing_student in self.students:
            if existing_student.roll_number == student.roll_number:
                raise ValueError("Duplicate roll number")

        self.students.append(student)

    def find_student_by_name(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student

        return None

    def find_student_by_roll_number(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student


class GradeBookIOError(Exception):
    """Raised when a GradeBook file operation fails."""
    pass


class Roster:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0.0

        total = sum(student.average() for student in self.students)
        return total / len(self.students)

    def save_to_file(self, path):
        try:
            with open(path, "w") as file:
                for student in self.students:
                    scores = ", ".join(str(score) for score in student.scores)
                    file.write(
                        f"{student.name},{student.roll_number},{scores}\n"
                    )
        except OSError as error:
            raise GradeBookIOError(
                f"Could not save roster to file: {path}"
            ) from error