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