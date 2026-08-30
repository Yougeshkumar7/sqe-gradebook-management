class Book:
    """Represents a library book."""

    def __init__(self, title, author):
        if not title.strip():
            raise ValueError("Book title cannot be empty")

        if not author.strip():
            raise ValueError("Book author cannot be empty")

   self.id_number = title
        self.author = author