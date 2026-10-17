
from lab8.src.gradebook import Student, Roster, rank_students


def test_rank_students_empty_roster_returns_empty_list():
    roster = Roster()
    assert rank_students(roster) == []


def test_rank_students_returns_single_student():
    roster = Roster()
    student = Student("Ali", "S001")
    student.scores = [80, 90]
    roster.add_student(student)
    assert rank_students(roster) == [student]


def test_rank_students_sorts_by_average_descending():
    roster = Roster()

    ali = Student("Ali", "S001")
    ali.scores = [70, 80]

    sara = Student("Sara", "S002")
    sara.scores = [90, 100]

    ahmed = Student("Ahmed", "S003")
    ahmed.scores = [80, 90]

    roster.add_student(ali)
    roster.add_student(sara)
    roster.add_student(ahmed)

    assert rank_students(roster) == [sara, ahmed, ali]
