import pytest

from gradebook import Student, Roster


@pytest.mark.parametrize("score_count", [0, 1, 2, 5, 6, 7])
def test_roster_score_count_boundary(score_count):
    student = Student("yougesh", "001")

    for score in range(score_count):
        student.add_score(score)

    roster = Roster()

    if score_count in [0, 7]:
        with pytest.raises(ValueError):
            roster.add_student(student)
    else:
        roster.add_student(student)
        assert student in roster.students