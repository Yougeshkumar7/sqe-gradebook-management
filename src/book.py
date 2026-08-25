class Book:
    """Represents a library book."""

    def __init__(self, title, author):
        if not title:
            raise ValueError("Book title cannot be empty")

        if not author:
            raise ValueError("Book author cannot be empty")

        self.title = title
        self.author = author