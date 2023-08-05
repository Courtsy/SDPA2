class Book:
    """
    This class is used to represent a book.

    Attributes:

    ISBN: str
        a string representation of the ISBN of the book
    title: str
        a string representation of the title of the book
    author: str
        a string representation of the author of the book
    number_of_copies: int
        an integer representing the number of copies of the book

    Methods:

    __str__():
        Returns a string representation of the book
    """
    def __init__(self, ISBN, title, author, number_of_copies):
        """
        This constructor method constructs all the necessary attributes for the book objects

        Parameters:

            ISBN: str
                a string representing the ISBN of the book
            title: str
                a string representing the title of the book
            author: str
                a string representing the author of the book
            number_of_copies: int
                an integer representing the number of copies of the book
        """
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.number_of_copies = number_of_copies

    def __str__(self):
        """
        This method returns a string representation of the book

        Returns:

        str
            a string representing the book in the format:
            "Title: {title}, Author: {author}, ISBN: {ISBN}, Copies Available: {number_of_copies}"

        """

        return f"Title: {self.title}, " \
               f"Author: {self.author}, " \
               f"ISBN: {self.ISBN}, " \
               f"Copies Available: {self.number_of_copies}"
