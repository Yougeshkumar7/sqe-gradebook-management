
import pytest
from src.gradebook import Student, GradeBook


# Test 1: Invalid score types
@pytest.mark.parametrize("score", [True, "90", None])
def test_grade_letter_invalid_type(score):
    student = Student("Ali", "101")

    with pytest.raises(TypeError):
        student.grade_letter(score)


# Test 2: Scores outside the valid range
@pytest.mark.parametrize("score", [-1, 101])
def test_grade_letter_invalid_range(score):
    student = Student("Ali", "101")

    with pytest.raises(ValueError):
        student.grade_letter(score)


# Test 3: Student name not found
def test_find_student_by_name_not_found():
    book = GradeBook()
    book.add_student(Student("Ali", "101"))
    book.add_student(Student("Sara", "102"))

    result = book.find_student_by_name("Ahmed")

    assert result is None


# Test 4: Roll number not found
def test_find_student_by_roll_number_not_found():
    book = GradeBook()
    book.add_student(Student("Ali", "101"))
    book.add_student(Student("Sara", "102"))

    result = book.find_student_by_roll_number("999")

    assert result is None


# Test 5: Different roll numbers are allowed
def test_add_students_with_different_roll_numbers():
    book = GradeBook()

    book.add_student(Student("Ali", "101"))
    book.add_student(Student("Sara", "102"))

    assert len(book.students) == 2
