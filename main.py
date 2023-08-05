# Importing each class from different files to be called upon in the main file
from member import Member
from book import Book
from library import Library

# Creating a library by calling the library class
library = Library()

# Adding books to the library by creating a catalogue of books to be selected from
# Follows a format of (ISBN, Book Title, Author Name, Number of copies available)
books = [
    Book('2943879088763', 'The Great Gatsby', 'F. Scott Fitzgerald', 5),
    Book('3679904055940', 'To Kill A Mockingbird', 'Harper Lee', 3),
    Book('5887213375927', 'Jane Eyre', 'Charlotte Bronte', 2),
    Book('6501436306213', 'Pride and Prejudice', 'Jane Austen', 7),
    Book('1517401882407', 'The Da Vinci Code', 'Dan Brown', 3),
    Book('7582354027903', 'Harry Potter and the Chamber of Secrets', 'J. K. Rowling', 8),
    Book('9404205148924', 'Black Beauty', 'Anna Sewell', 1),
    Book('4313218235661', 'The Hite Report', 'Shere Hite', 4),
    Book('9153125301016', 'The Hunger Games', 'Suzanne Collins', 6),
    Book('2261487960075', 'The Godfather', 'Mario Puzo', 4),
    Book('8349882841851', 'Gone Girl', 'Gillian Flynn', 2),
    Book('2695557253203', 'Jaws', 'Peter Benchley', 3),
]
for book in books:
    library.add_book(book)

# Create a member
members = [
    Member('001', 'John Doe'),
    Member('002', 'Jane Smith'),
    Member('003', 'Jack Robinson'),
    Member('004', 'Jill Green'),
    Member('005', 'Harry Wilson')
]

while True:
    # Prompt for member ID
    current_member = None
    while current_member is None:
        print("Welcome to the library!")
        entered_ID = input("Please enter your member ID to log in: ")
        for member in members:
            if member.ID == entered_ID:
                current_member = member
                break

        if current_member:
            print(f"Welcome, {current_member.name}!")
        else:
            print("Error: Member ID not recognized. Please type a valid member ID.")

    while True:
        print("\nPlease select an option below.")
        print("1. Display available books")
        print("2. Inquire about a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Log out")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            print("Here are the available books: ")
            library.display_books()
        elif choice == '2':
            ISBN = input("Enter ISBN (or leave blank): ")
            title = None
            author = None
            if not ISBN:
                title = input("Enter title (or leave blank): ")
            if not ISBN and not title:
                author = input("Enter author (or leave blank): ")

            current_member.inquire(library, ISBN=ISBN, title=title, author=author)
        elif choice == '3':
            while True:  # Start a loop that will continue until a valid ISBN is entered
                ISBN = input("Enter the 13-digit ISBN of the book you want to borrow: ")
                if len(ISBN) != 13 or not ISBN.isdigit():
                    print("Error: ISBN must be a 13-digit number.")
                    continue  # Continue to the next iteration of the loop if the ISBN is not valid
                # Get the list of available books from the library
                available_books = library.get_books()

                # Check if the ISBN matches one of the available books in the catalogue
                if any(book.ISBN == ISBN for book in available_books):
                    break  # Exit the loop if a matching book is found
                else:
                    print("Error: No book with that ISBN is available in the catalogue.")

            while True:  # Start a loop that will continue until a valid number of days is entered
                try:
                    days = int(input("Enter the number of days you want to borrow the book for: "))
                    if days <= 0:
                        raise ValueError("Must be a valid number of days")
                    library.process_borrow_request(current_member, ISBN, days)
                    break  # Exit the loop if a valid number of days was entered
                except ValueError as e:
                    print(e)  # Print the error message and continue to the next iteration of the loop

        elif choice == '4':
            ISBN = input("Enter ISBN of the book you want to return: ")
            library.process_return_request(current_member, ISBN)
        elif choice == '5':
            print(f"Goodbye, {current_member.name}!")
            break  # Break out of the main menu loop to return to member selection
        elif choice == '6':
            print("Thanks for visiting the library. Have a great day!")
            exit()
        if choice != '1' and choice != '6':
            print("\nCurrent catalogue:")
            library.display_books()
        elif choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please select option 1,2,3,4,5 or 6")
