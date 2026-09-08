import pytest
from lab5.src.gradebook import Student, Roster


def test_zero_scores_invalid():
    roster = Roster()
    student = Student("Ali", 101)

    with pytest.raises(ValueError):
        roster.add_student(student)


def test_three_scores_valid():
    roster = Roster()
    student = Student("Ali", 102)

    student.add_score(70)
    student.add_score(80)
    student.add_score(90)

    roster.add_student(student)

    assert len(roster.students) == 1


def test_eight_scores_invalid():
    roster = Roster()
    student = Student("Ahmed", 103)

    for i in range(8):
        student.add_score(70)

    with pytest.raises(ValueError):
        roster.add_student(student)