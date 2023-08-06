# Thomas Courts - 2344550

class Library:
    """
    This class is used to represent a library.

    Attributes:

    books: list
        a list of Book objects that the library has

    Methods:
    add_book(book)
        Adds a book to the library's list of books.
    get_books()
        Returns the list of books in the library.
    update_book_copies(ISBN, change)
        Updates the number of copies of a book in the library.
    display_books()
        Prints out all the books in the library.
    process_borrow_request(member, ISBN, days)
        Processes a member's request to borrow a book.
    process_return_request(member, ISBN)
        Processes a member's request to return a book.

    """
    def __init__(self):
        """This constructor method constructs the necessary attributes for the library objects,
        which is a list of books"""
        self.books = []

    def add_book(self, book):
        """Adds a book to the library's list of books"""
        self.books.append(book)

    def get_books(self):
        """Returns the list of books in the library"""
        return self.books

    def update_book_copies(self, ISBN, change):
        """Updates the number of copies of a book in the library

        Parameters:
            ISBN: str
                the ISBN of the book to update
            change: int
                the amount to change the number of copies by
        """
        for book in self.books:
            if book.ISBN == ISBN:
                book.number_of_copies += change
                return

    def display_books(self):
        """Prints out (displays) all the books in the library"""
        for book in self.books:
            print(book)

    def process_borrow_request(self, member, ISBN, days):
        """
        Processes a member's request to borrow a book

        Parameters:

            member: Member
                the member who wants to borrow the book
            ISBN: str
                the ISBN of the book to borrow
            days: int
                the number of days to borrow the book for
        """
        member.borrow(self, ISBN, days)

    def process_return_request(self, member, ISBN):
        """
        Processes a member's request to return a book

        Parameters:

            member: Member
                the member who wants to return the book
            ISBN: str
                the ISBN of the book to return
        """
        member.return_book(self, ISBN)
