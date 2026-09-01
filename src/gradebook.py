class Student:
    def __init__(self, name, roll_number):
        if not roll_number:
            raise ValueError("Student ID cannot be empty")

        self.name = name
        self.roll_number = roll_number
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)
