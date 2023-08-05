class Member:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.totalCheckedOutBooks = 0
        self.borrowed_books = []

    def inquire(self, library, ISBN=None, title=None, author=None):
        found = False
        books = library.get_books()
        if ISBN:
            for book in books:
                if book.ISBN == ISBN:
                    print(f"Title: {book.title}, Author: {book.author}, Copies Available: {book.number_of_copies}")
                    found = True
        elif title:
            for book in books:
                if book.title == title:
                    print(f"ISBN: {book.ISBN}, Author: {book.author}, Copies Available: {book.number_of_copies}")
                    found = True
        elif author:
            for book in books:
                if book.author == author:
                    print(f"ISBN: {book.ISBN}, Title: {book.title}, Copies Available: {book.number_of_copies}")
                    found = True
        if not found:
            print("The book you're looking for is not available in the library.")

    def borrow(self, library, ISBN, days):
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

            # Print a success message
            print(f"You have borrowed one book with title {book_to_borrow.title}, {ISBN} for {days} days.")
        else:
            # Print an error message
            print("The book you're trying to borrow is not available.")

    def return_book(self, library, ISBN):
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

            # Print a success message
            print(f"You have returned the book with title {book_to_return.title}, {ISBN}. Thank you!")
            print(f"Receipt: {self.name} returned {book_to_return.title}")
        else:
            # Print an error message
            print("The book you're trying to return was not borrowed by you.")