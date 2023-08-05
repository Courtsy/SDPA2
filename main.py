from member import Member
from book import Book
from library import Library

# Create a library
library = Library()

# Add some books to the library
books = [
    Book('1234567890', 'Book Title 1', 'Author 1', 5),
    Book('0987654321', 'Book Title 2', 'Author 2', 3),
]
for book in books:
    library.add_book(book)

# Create a member
member = Member('001', 'John Doe')

# User interface
while True:
    print("\n1. Display available books")
    print("2. Inquire about a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        library.display_books()
    elif choice == '2':
        ISBN = input("Enter ISBN (or leave blank): ")
        title = input("Enter title (or leave blank): ")
        member.inquire(library, ISBN=ISBN, title=title)
    elif choice == '3':
        ISBN = input("Enter ISBN of the book you want to borrow: ")
        days = int(input("Enter the number of days you want to borrow the book for: "))
        library.process_borrow_request(member, ISBN, days)
    elif choice == '4':
        ISBN = input("Enter ISBN of the book you want to return: ")
        library.process_return_request(member, ISBN)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
