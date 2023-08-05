from member import Member
from book import Book
from library import Library

# Create a library
library = Library()

# Add some books to the library
books = [
    Book('1234567890456', 'Book Title 1', 'Author 1', 5),
    Book('0987654321236', 'Book Title 2', 'Author 2', 3),
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

                    # Check if the ISBN matches one of the available books in the catalogue                available_books = library.get_books()
                if any(book.ISBN == ISBN for book in available_books):
                    break  # Exit the loop if a matching book is found
                else:
                    print("Error: No book with that ISBN is available in the catalogue.")

            while True:  # Start a loop that will continue until a valid number of days is entered
                try:
                    days = int(input("Enter the number of days you want to borrow the book for: "))
                    if days <= 0:
                        raise ValueError("Must be a valid number of days")
                    library.process_borrow_request(member, ISBN, days)
                    break  # Exit the loop if a valid number of days was entered
                except ValueError as e:
                    print(e)  # Print the error message and continue to the next iteration of the loop

        elif choice == '4':
            ISBN = input("Enter ISBN of the book you want to return: ")
            library.process_return_request(member, ISBN)
        elif choice == '5':
            print(f"Goodbye, {current_member.name}!")
            break  # Break out of the main menu loop to return to member selection
        elif choice == '6':
            print("Thanks for visiting the library. Have a great day!")
            exit()
        if choice != '1' and choice != '6':
            print("\nCurrent catalogue:")
            library.display_books()
        else:
            print("Invalid choice. Please select option 1,2,3,4,5 or 6")


