import pytest

from src.gradebook import GradeBook, Student, percentile


def make_roster(*scores):
    roster = GradeBook()
    for index, score in enumerate(scores, start=1):
        student = Student(f"Student {index}", str(index))
        student.add_score(score)
        roster.add_student(student)
    return roster


def test_percentile_uses_peer_count_independent_of_roster_order():
    roster = make_roster(90, 25, 70)

    assert [percentile(student, roster) for student in roster.students] == [
        100.0, 0.0, 50.0
    ]
    assert [student.average() for student in roster.students] == [90, 25, 70]


def test_tied_averages_share_a_percentile():
    roster = make_roster(25, 70, 70, 90)
    first, second = roster.students[1:3]

    assert percentile(first, roster) == pytest.approx(100.0 / 3)
    assert percentile(second, roster) == percentile(first, roster)


def test_single_student_receives_100_percentile():
    roster = make_roster(70)

    assert percentile(roster.students[0], roster) == 100.0


def test_empty_roster_raises_value_error():
    with pytest.raises(ValueError, match="empty roster"):
        percentile(Student("Absent", "99"), GradeBook())


def test_missing_roll_number_raises_value_error():
    with pytest.raises(ValueError, match="not in the roster"):
        percentile(Student("Absent", "99"), make_roster(70))


def test_uses_scores_from_roster_entry():
    roster = make_roster(25, 90)
    detached = Student("Stale copy", "2")
    detached.add_score(10)

    assert percentile(detached, roster) == 100.0
