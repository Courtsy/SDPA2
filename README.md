# SDPA2
SDPA Coursework

Part 1 : Object Oriented Programming - Code Design

To run the code simply click run in the main.py file

book.py:

This file contains the Book class that holds everything related to the book in the library. It holds a constructor method __init__ that constructs the necessary attributes for the book objects that include the ISBN, title, author and number of copies that are all necessary for the creation of the library. It also holds another constructor method __str__ that is used to return the string representation of a book. It allows for a convenient way to display the details of a book in a formatted manner.

library.py:

This file contains the Library class that holds everything related to representing the library. It holds several methods that are all used to create and maintain the library. It holds a constructor method __init__ that lists the books. Add_book that allows a book to be added to the library, get_books that returns the list of books in the library. Update_book_copies that updates the number of copies of a book in the library, display_books that displays all the books in the library. Finally, two methods, process_borrow_request and process_return_request that process the member's borrow and return requests respectively.

member.py:

This file contains the Member class that holds everything representing a library member. Again, this class contains a constructor method __init__ that constructs the necessary attributes for a member object, an inquire method that allows a member to inquire about a book in the library based on different parameters. An _search_books method which is a helper method that searches for a book in the list of books. A borrow method that allows a member to borrow a book and also updates the members borrowed books and updates the number of copies in the library. Finally, a return_book method that is similar to the borrow method except it does the opposite by returning a book to the library by reducing a members borrowed books and updates the number of copies in the library.

main.py:

This file is where the code is run and the library is created and displayed to the user. All classes are imported and used in this file. It holds the list of books used in the library along with the different members list. A loop is used to create the user interface for the library that gives the member several options to choose from. There are several other loops used for each option that also handles errors. 

I have used no other libraries for this code other than the standard python library.

I encountered several design choices when creating the library. Initially, I decided to just create and map out which methods I would need for each class for the library to work. I realised that the book.py file would only need constructor methods that holds the details of each book. For the library.py file I understood that I needed to focus on what would be needed to construct the library and for it to work along the other classes. The member.py file was slightly trickier than the others to create as it needed several design changes to handle errors that were found when running the code many times. I decided to make as many methods as possible to make sure that my code is clear and understandable which allows for easier problem solving when encounting errors. When designing the user interface in the main.py file I decided to create a simple interface first that worked and then update it to handle errors as I found them. I added a member ID log in later on when I felt that I was happy with my user interface and handling all errors, along with populating more members and books to complete the library. 

Part 2: Data Analytics

I decided to take a lot of time searching for a sound dataset that was robust enough to be able to analyse. After finding a dataset that I was happy with I found that there was a lot of data preparation and cleaning needed. I did not encounter too many issues with this section. 

All of my documentation for this section is in my jupyter notebook file.

Packages used for data analytics:

matplotlib.pyplot
pandas
seaborn
numpy
scipy.stats