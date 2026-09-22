import pytest

from src.gradebook import Student, GradeBook


def test_student_creation():
    student = Student("Ali", "001")

    assert student.name == "Ali"
    assert student.roll_number == "001"
    assert student.scores == []


def test_student_id_cannot_be_empty():
    with pytest.raises(ValueError):
        Student("Ali", "")


def test_add_valid_score():
    student = Student("Ali", "001")

    student.add_score(85)

    assert student.scores == [85]


def test_add_negative_score():
    student = Student("Ali", "001")

    with pytest.raises(ValueError):
        student.add_score(-1)


def test_add_score_greater_than_100():
    student = Student("Ali", "001")

    with pytest.raises(ValueError):
        student.add_score(101)


def test_add_non_numeric_score():
    student = Student("Ali", "001")

    with pytest.raises(TypeError):
        student.add_score("85")


def test_average_with_no_scores():
    student = Student("Ali", "001")

    assert student.average() == 0.0


def test_average():
    student = Student("Ali", "001")

    student.add_score(80)
    student.add_score(90)

    assert student.average() == 85.0


def test_grade_letter_A():
    student = Student("Ali", "001")

    assert student.grade_letter(85) == "A"


def test_grade_letter_B():
    student = Student("Ali", "001")

    assert student.grade_letter(75) == "B"


def test_grade_letter_C():
    student = Student("Ali", "001")

    assert student.grade_letter(65) == "C"


def test_grade_letter_D():
    student = Student("Ali", "001")

    assert student.grade_letter(55) == "D"


def test_grade_letter_F():
    student = Student("Ali", "001")

    assert student.grade_letter(45) == "F"


def test_duplicate_roll_number():
    gradebook = GradeBook()

    student1 = Student("Ali", "001")
    student2 = Student("Ahmed", "001")

    gradebook.add_student(student1)

    with pytest.raises(ValueError):
        gradebook.add_student(student2)


def test_find_student_by_name():
    gradebook = GradeBook()

    student = Student("Ali", "001")
    gradebook.add_student(student)

    result = gradebook.find_student_by_name("Ali")

    assert result == student


def test_find_student_by_roll_number():
    gradebook = GradeBook()

    student = Student("Ali", "001")
    gradebook.add_student(student)

    result = gradebook.find_student_by_roll_number("001")

    assert result == student


# Issue #18: Boolean values must not be accepted as scores

def test_boolean_true_is_not_valid_score():
    student = Student("Ali", "002")

    with pytest.raises(TypeError):
        student.add_score(True)


def test_boolean_false_is_not_valid_score():
    student = Student("Ali", "003")

    with pytest.raises(TypeError):
        student.add_score(False)


# Issue #19: Student name must not be empty or invalid

def test_empty_student_name_is_invalid():
    with pytest.raises(ValueError):
        Student("", "004")


def test_whitespace_student_name_is_invalid():
    with pytest.raises(ValueError):
        Student("   ", "005")


def test_none_student_name_is_invalid():
    with pytest.raises(TypeError):
        Student(None, "006")