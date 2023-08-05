class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        # Add a book to the library
        self.books.append(book)

    def get_books(self):
        return self.books

    def update_book_copies(self, ISBN, change):
        for book in self.books:
            if book.ISBN == ISBN:
                book.number_of_copies += change
                return

    def display_books(self):
        # Display available books
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.ISBN}, Copies Available: {book.number_of_copies}")

    def process_borrow_request(self, member, ISBN, days):
        # Process borrowing requests from member
        member.borrow(self, ISBN, days)
    def process_return_request(self, member, ISBN):
        # Process returning requests and update the catalogue
        member.return_book(self, ISBN)
