from src.gradebook import GradeBook, Student, percentile


def test_lowest_average_has_zero_percentile():
    roster = GradeBook()
    low = Student("Low", "1")
    low.add_score(25)
    high = Student("High", "2")
    high.add_score(90)
    roster.add_student(low)
    roster.add_student(high)

    assert percentile(low, roster) == 0.0
