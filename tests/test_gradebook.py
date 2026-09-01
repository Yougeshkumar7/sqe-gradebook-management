from src.gradebook import Student


def test_average_with_no_scores_returns_zero():
    student = Student("Ali", 101)
    assert student.average() == 0.0
