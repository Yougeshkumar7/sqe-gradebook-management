import pytest

from gradebook import Student, Roster


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


# Test 1
def test_student_creation(student):
    assert student.name == "Ali"
    assert student.roll_number == "001"
    assert student.scores == []


# Test 2
def test_add_valid_score(student):
    student.add_score(85)

    assert student.scores == [85]


# Test 3
def test_average(student):
    student.add_score(80)
    student.add_score(90)

    assert student.average() == 85.0


# Test 4
def test_grade_letter(student):
    assert student.grade_letter(85) == "A"


# Test 5 - using module-scope fixture
def test_roster_add_student(roster, student):
    roster.add_student(student)

    assert student in roster.students