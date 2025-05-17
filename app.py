# PERSONAL LIBRARY MANAGER
import json

# File to store the library
LIBRARY_FILE = "library.txt"

# Load the library from a file
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save the library to a file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a book to the library
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = input("Enter the publication year: ").strip()
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    # Validate year input
    if not year.isdigit():
        print("Invalid year! Please enter a number.")
        return

    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    }
    
    library.append(book)
    print("Book added successfully!")

# Remove a book from the library
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found!")

# Search for books by title or author
def search_books(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()

    if choice not in ["1", "2"]:
        print("Invalid choice!")
        return

    query = input("Enter the title or author: ").strip().lower()
    results = [
        book for book in library
        if (choice == "1" and book["title"].lower() == query) or
           (choice == "2" and book["author"].lower() == query)
    ]

    if results:
        print("\nMatching Books:")
        for i, book in enumerate(results, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

# Display all books in the library
def display_books(library):
    if not library:
        print("Your library is empty!")
        return

    print("\nYour Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Display library statistics
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("Your library is empty!")
        return

    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100

    print(f"\nTotal books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

# Menu system
def main():
    library = load_library()

    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
