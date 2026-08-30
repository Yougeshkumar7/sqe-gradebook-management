from src.book import Book


def test_book_creation():
    book = Book("Harry Potter", "J.K. Rowling")

    assert book.student_id == "Harry Potter"
    assert book.author == "J.K. Rowling"


def test_empty_title_raises_error():
    try:
        Book("", "J.K. Rowling")
        assert False
    except ValueError:
        assert True


def test_empty_author_raises_error():
    try:
        Book("Harry Potter", "")
        assert False
    except ValueError:
        assert True