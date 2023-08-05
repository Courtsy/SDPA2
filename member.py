class Member:
    """
    This class is used to represent a Library Member.

    Attributes:

    ID: str
        a unique identifier for the member
    name: str
        the member's name
    totalCheckedOutBooks: int
        the total number of books the member has checked out
    borrowed_books: list
        a list of Book objects that the member has borrowed

    Methods:

    inquire(library, ISBN=None, title=None, author=None)
        Inquires about a book in the library.
    _search_books(books, search_term, attribute)
        Helper method to search for a book in a list of books.
    borrow(library, ISBN, days)
        Borrows a book from the library.
    return_book(library, ISBN)
        Returns a book to the library.
    """
    def __init__(self, ID, name):
        """This constructor method constructs the necessary attributes for the member object"""
        self.ID = ID
        self.name = name
        self.totalCheckedOutBooks = 0
        self.borrowed_books = []

    def inquire(self, library, ISBN=None, title=None, author=None):
        """
        Inquires about a book in the library based on its ISBN, title or author

        Parameters:
            library: Library
                the library to inquire in
            ISBN: str (optional)
                the ISBN of the book to inquire about
            title: str (optional)
                the title of the book to inquire about
            author: str (optional)
                the author of the book to inquire about
        """

        # Get the list of all books in the library
        books = library.get_books()
        # If an ISBN is provided, search for the books with that ISBN
        if ISBN:
            self._search_books(books, ISBN, 'ISBN')
        # If a title is provided (no ISBN), search for books with that title
        elif title:
            self._search_books(books, title, 'title')
        # If an author is provided (no ISBN or title), then search for books by that author
        elif author:
            self._search_books(books, author, 'author')
        # If none of these are provided, then print an error message
        else:
            print("The book you're looking for is not available in the library.")

    def _search_books(self, books, search_term, attribute):
        """Helper method to search for a book in a list of books"""
        # Initialising a variable to track whether a book has been found
        found = False
        # Iterating over each book in a list of books
        for book in books:
            # If the attribute of the book matches the search term, print the book's details
            if getattr(book, attribute) == search_term:
                print(f"ISBN: {book.ISBN}, "
                      f"Title: {book.title}, "
                      f"Author: {book.author}, "
                      f"Copies Available: {book.number_of_copies}")
                # Set the found variable to True since a book has been found
                found = True
        # If no book was found that matches the search term , then print a message that no book what that attribute
        # is available
        if not found:
            print(f"No book with that {attribute} is available in the library.")

    def borrow(self, library, ISBN, days):
        """Borrows a book from the library"""
        # Search for the book in the library's catalogue
        book_to_borrow = None
        for book in library.get_books():
            if book.ISBN == ISBN:
                book_to_borrow = book
                break

        # Check if the book is available
        if book_to_borrow and book_to_borrow.number_of_copies > 0:
            # Reduce the number of copies of the book in the library
            book_to_borrow.number_of_copies -= 1

            # Add the book to the member's borrowed books
            self.borrowed_books.append((book_to_borrow, days))
            self.totalCheckedOutBooks += 1

            # Print a message confirming that you have borrowed a book
            print(f"You have borrowed one book with title {book_to_borrow.title}, {ISBN} for {days} days.")
        else:
            # Print an error message
            print("The book you're trying to borrow is not available.")

    def return_book(self, library, ISBN):
        """Returns a book to the library"""
        # Search for the book in the member's borrowed books
        book_to_return = None
        for book, days in self.borrowed_books:
            if book.ISBN == ISBN:
                book_to_return = book
                break

        # Check if the book is found
        if book_to_return:
            # Increase the number of copies of the book in the library
            library.update_book_copies(ISBN, 1)

            # Remove the book from the member's borrowed books
            self.borrowed_books.remove((book_to_return, days))
            self.totalCheckedOutBooks -= 1

            # Print a message saying the book has been returned along with the receipt
            print(f"You have returned the book with title {book_to_return.title}, {ISBN}. Thank you!")
            print(f"Receipt: {self.name} returned {book_to_return.title}")
        else:
            # Print an error message
            print("The book you're trying to return was not borrowed by you.")
