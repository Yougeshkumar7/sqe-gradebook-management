from src.gradebook import Student


def test_average_with_no_scores_returns_zero():
    student = Student("Ali", 101)
    assert student.average() == 0.0


def test_empty_student_id_raises_error():
    try:
        Student("Ali", "")
        assert False
    except ValueError:
        assert True
