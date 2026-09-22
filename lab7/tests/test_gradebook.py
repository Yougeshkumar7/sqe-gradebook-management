import pytest

from gradebook import Student, Roster, GradeBookIOError


# Function scope is useful when every test needs a fresh object.
# A new Student is created for each test, so tests stay independent.
@pytest.fixture
def student():
    return Student("Ali", "001")


# Module scope is useful when setup can be reused by multiple tests
# in the same file and does not need to be recreated for every test.
@pytest.fixture(scope="module")
def roster():
    return Roster()


# =========================
# Task 1 - Fixtures
# =========================

def test_student_creation(student):
    assert student.name == "Ali"
    assert student.roll_number == "001"
    assert student.scores == []


def test_add_valid_score(student):
    student.add_score(85)

    assert student.scores == [85]


def test_average(student):
    student.add_score(80)
    student.add_score(90)

    assert student.average() == 85.0


def test_grade_letter(student):
    assert student.grade_letter(85) == "A"


def test_roster_add_student(roster, student):
    roster.add_student(student)

    assert student in roster.students


# =========================
# Task 2 - class_average()
# =========================

def test_class_average_empty_roster():
    roster = Roster()

    assert roster.class_average() == 0.0


def test_class_average_single_student():
    roster = Roster()

    student = Student("Sara", "002")
    student.add_score(80)
    student.add_score(90)

    roster.add_student(student)

    assert roster.class_average() == 85.0


def test_class_average_multiple_students():
    roster = Roster()

    student1 = Student("Ali", "003")
    student1.add_score(80)
    student1.add_score(90)

    student2 = Student("Sara", "004")
    student2.add_score(70)

    roster.add_student(student1)
    roster.add_student(student2)

    assert roster.class_average() == 77.5


# =========================
# Task 3 - Mocking File I/O
# =========================

def test_save_to_file(mocker):
    roster = Roster()

    student = Student("Ali", "005")
    student.add_score(80)
    student.add_score(90)

    roster.add_student(student)

    mock_open = mocker.patch(
        "builtins.open",
        mocker.mock_open()
    )

    roster.save_to_file("students.txt")

    mock_open.assert_called_once_with("students.txt", "w")

    handle = mock_open()
    handle.write.assert_called_once_with(
        "Ali,005,80, 90\n"
    )


def test_save_to_file_os_error(mocker):
    roster = Roster()

    mocker.patch(
        "builtins.open",
        side_effect=OSError("Permission denied")
    )

    with pytest.raises(GradeBookIOError):
        roster.save_to_file("students.txt")