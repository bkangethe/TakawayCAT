class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
        else:
            print(f"Sorry, '{book.title}' is already borrowed by another member.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
        else:
            print(f"'{book.title}' is not in your borrowed books list.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"Books borrowed by {self.name}:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")


# Interactive code
def main():
    # Create some books and a library member
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    member = LibraryMember("Alice", "M001")

    while True:
        print("\nLibrary System")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. List Borrowed Books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Books:")
            for i, book in enumerate([book1, book2, book3], start=1):
                status = "Available" if not book.is_borrowed else "Not Available"
                print(f"{i}. {book.title} by {book.author} - {status}")
            
            book_choice = input("Enter the number of the book you want to borrow: ")
            if book_choice == "1":
                member.borrow_book(book1)
            elif book_choice == "2":
                member.borrow_book(book2)
            elif book_choice == "3":
                member.borrow_book(book3)
            else:
                print("Invalid choice. Please try again.")

        elif choice == "2":
            print("\nReturning a Book")
            member.list_borrowed_books()
            book_title = input("Enter the title of the book you want to return: ")

            # Find the book by title in borrowed_books
            book_to_return = None
            for book in member.borrowed_books:
                if book.title == book_title:
                    book_to_return = book
                    break
            
            if book_to_return:
                member.return_book(book_to_return)
            else:
                print(f"No borrowed book with title '{book_title}' was found.")

        elif choice == "3":
            member.list_borrowed_books()

        elif choice == "4":
            print("Exiting the library system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
