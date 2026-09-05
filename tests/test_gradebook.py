from src.gradebook import Student, GradeBook


def test_add_score_valid_input():
    student = Student("Ali", 101)

    student.add_score(85)

    assert student.scores == [85]


def test_add_score_negative_input():
    student = Student("Ali", 101)

    try:
        student.add_score(-5)
        assert False
    except ValueError:
        assert student.scores == []


def test_add_score_non_numeric_input():
    student = Student("Ali", 101)

    try:
        student.add_score("abc")
        assert False
    except TypeError:
        assert student.scores == []


def test_average_with_scores():
    student = Student("Ali", 101)

    student.add_score(80)
    student.add_score(90)

    assert student.average() == 85.0


def test_average_with_empty_list():
    student = Student("Ali", 101)

    assert student.average() == 0.0


def test_average_with_single_score():
    student = Student("Ali", 101)

    student.add_score(75)

    assert student.average() == 75.0


def test_duplicate_roll_number_rejection():
    gradebook = GradeBook()

    student1 = Student("Ali", 101)
    student2 = Student("Ahmed", 101)

    gradebook.add_student(student1)

    try:
        gradebook.add_student(student2)
        assert False
    except ValueError:
        assert len(gradebook.students) == 1


def test_name_case_insensitivity():
    gradebook = GradeBook()

    student = Student("Ali", 101)
    gradebook.add_student(student)

    found_student = gradebook.find_student_by_name("ali")

    assert found_student is student


def test_maximum_score_boundary():
    student = Student("Ali", 101)

    student.add_score(100)

    assert student.scores == [100]


def test_minimum_score_boundary():
    student = Student("Ali", 101)

    student.add_score(0)

    assert student.scores == [0]


def test_grade_letter_mid_range():
    student = Student("Ali", 101)

    assert student.grade_letter(75) == "B"


def test_grade_letter_boundary():
    student = Student("Ali", 101)

    assert student.grade_letter(80) == "A"