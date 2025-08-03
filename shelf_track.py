import sqlite3
import os

def create_database():
    """Create a SQLite database and tables populated 
    with initial data."""
    try:
        with sqlite3.connect('ebookstore.db') as conn:
            c = conn.cursor()
            # Create author table if it does not exist
            c.execute('''
                CREATE TABLE IF NOT EXISTS author (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    country TEXT NOT NULL
                )
            ''')
            # Create book table with foreign key reference to author
            c.execute('''
                CREATE TABLE IF NOT EXISTS book (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    authorID INTEGER NOT NULL,
                    qty INTEGER NOT NULL,
                    FOREIGN KEY (authorID) REFERENCES author(id)
                )
            ''')
            # Verify if data already exists
            c.execute("SELECT COUNT(*) FROM author")
            if c.fetchone()[0] == 0:
                # Insert initial data into author table
                authors = [
                    (1290, "Charles Dickens", "England"),
                    (8937, "J.K. Rowling", "England"),
                    (2356, "C.S. Lewis", "Ireland"),
                    (6380, "J.R.R. Tolkien", "South Africa"),
                    (5620, "Lewis Carroll", "England")
                ]
                c.executemany("INSERT INTO author VALUES (?, ?, ?)", authors)

                # Insert books into book table
                books = [
                    (3001, "A Tale of Two Cities", 1290, 30),
                    (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
                    (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
                    (3004, "The Lord of the Rings", 6380, 37),
                    (3005, "Alice's Adventures in Wonderland", 5620, 12)
                ]
                c.executemany("INSERT INTO book VALUES (?, ?, ?, ?)", books)
                print("Database initialized with sample data.")
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def validate_book_id(book_id):
    """Validate book ID - must be 4 digits."""
    try:
        book_id = int(book_id)
        if len(str(book_id)) != 4 or book_id <= 0:
            return None
        return book_id
    except ValueError:
        return None
    
def validate_author_id(author_id):
    """Validate author ID - must be 4 digits."""
    try:
        author_id = int(author_id)
        if len(str(author_id)) != 4 or author_id <= 0:
            return None
        return author_id
    except ValueError:
        return None
    
def validate_quantity(qty):
    """Validate quantity - must be a positive integer."""
    try:
        qty = int(qty)
        if qty < 0:
            return None
        return qty
    except ValueError:
        return None
    
def add_book():
    """Add new book to the database."""
    print("\n--- ADD NEW BOOK ---")
    
    try:
        book_id = input("Enter book ID (4 digits): ")
        book_id = validate_book_id(book_id)
        if book_id is None:
            print("Error: Book ID must be 4 digits positive integer.")
            return
    
        title = input("Enter book title: ")
        if not title:
            print("Error: Book title must not be empty.")
            return
    
        author_id_input = input("Enter author ID (4 digits): ")
        author_id = validate_author_id(author_id_input)
        if author_id is None:
            print("Error: Author ID must be 4 digits positive integer.")
            return
    
        qty_input = input("Enter quantity (positive integer): ")
        qty = validate_quantity(qty_input)
        if qty is None:
            print("Error: Quantity must be a positive integer.")
            return
        
        # Add to database
        with sqlite3.connect('ebookstore.db') as conn:
            c = conn.cursor()

            # Verify if author exists
            c.execute("SELECT id FROM author WHERE id = ?", (author_id,))
            if not c.fetchone():
                print(f"Error: Author ID {author_id} does not exist.")
                return
            
            # Verify if the book ID already exists
            c.execute("SELECT id FROM book WHERE id = ?", (book_id,))
            if c.fetchone():
                print(f"Error: Book ID {book_id} already exists.")
                return
            
            # Insert book into the database
            c.execute("INSERT INTO book VALUES (?, ?, ?, ?)",
                      (book_id, title, author_id, qty))
            conn.commit()
            print(f"Book '{title}' added successfully!")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")

def update_book():
    """Update book information with author ID validation."""
    print("\n--- UPDATE BOOK ---")
    
    try:
        book_id_input = input("Enter book ID to update: ")
        book_id = validate_book_id(book_id_input)
        if book_id is None:
            print("Error: Book ID must be 4 digits.")
            return
        
        with sqlite3.connect('ebookstore.db') as conn:
            c = conn.cursor()
            
            # Get current book info with author details
            c.execute('''
                SELECT b.id, b.title, b.qty, a.name, a.country, a.id as author_id
                FROM book b
                JOIN author a ON b.authorID = a.id
                WHERE b.id = ?
            ''', (book_id,))
            
            book_info = c.fetchone()
            if not book_info:
                print(f"Error: Book with ID {book_id} not found.")
                return
            
            # Display current information
            print(f"\nCurrent information:")
            print(f"Title: {book_info[1]}")
            print(f"Author: {book_info[3]} ({book_info[4]})")
            print(f"Quantity: {book_info[2]}")
            
            # Update options
            print("\nWhat would you like to update?")
            print("1. Quantity")
            print("2. Title")
            print("3. Author ID")
            print("4. Author name/country")
            print("0. Cancel")
            
            choice = input("Select option: ").strip()
            
            if choice == "1":
                # Update quantity
                new_qty_input = input("Enter new quantity: ")
                new_qty = validate_quantity(new_qty_input)
                if new_qty is None:
                    print("Error: Quantity must be positive integer.")
                    return
                
                c.execute("UPDATE book SET qty = ? WHERE id = ?", (new_qty, book_id))
                conn.commit()
                print("Quantity updated successfully!")
                
            elif choice == "2":
                # Update title
                new_title = input("Enter new title: ").strip()
                if not new_title:
                    print("Error: Title cannot be empty.")
                    return
                
                c.execute("UPDATE book SET title = ? WHERE id = ?", (new_title, book_id))
                conn.commit()
                print("Title updated successfully!")
                
            elif choice == "3":
                # Update author ID (with validation)
                new_author_id_input = input("Enter new author ID: ")
                new_author_id = validate_author_id(new_author_id_input)
                if new_author_id is None:
                    print("Error: Author ID must be 4 digits.")
                    return
                
                c.execute("SELECT id FROM author WHERE id = ?", (new_author_id,))
                if not c.fetchone():
                    print(f"Error: Author ID {new_author_id} does not exist.")
                    return
                
                c.execute("UPDATE book SET authorID = ? WHERE id = ?", (new_author_id, book_id))
                conn.commit()
                print("Author ID updated successfully!")
                
            elif choice == "4":
                # Update author name/country
                author_id = book_info[5]
                
                update_name = input("Update author name? (y/n): ").lower() == 'y'
                update_country = input("Update author country? (y/n): ").lower() == 'y'
                
                if update_name:
                    new_name = input("Enter new author name: ").strip()
                    if new_name:
                        c.execute("UPDATE author SET name = ? WHERE id = ?", (new_name, author_id))
                
                if update_country:
                    new_country = input("Enter new country: ").strip()
                    if new_country:
                        c.execute("UPDATE author SET country = ? WHERE id = ?", (new_country, author_id))
                
                if update_name or update_country:
                    conn.commit()
                    print("Author information updated successfully!")
                else:
                    print("No changes made.")
                    
            elif choice == "0":
                print("Update cancelled.")
            else:
                print("Invalid choice.")
                
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")

def delete_book():
    """Delete a book from the database."""
    print("\n--- DELETE BOOK ---")
    
    try:
        book_id_input = input("Enter book ID to delete: ")
        book_id = validate_book_id(book_id_input)
        if book_id is None:
            print("Error: Book ID must be 4 digits.")
            return
        
        with sqlite3.connect('ebookstore.db') as conn:
            c = conn.cursor()
            
            # Retrieve book information for confirmation
            c.execute('''
                SELECT b.title, a.name
                FROM book b
                JOIN author a ON b.authorID = a.id
                WHERE b.id = ?
            ''', (book_id,))

            book_info = c.fetchone()
            if not book_info:
                print(f"Error: Book with ID {book_id} does not exist.")
                return
            
            print(f"\nBook to delete:")
            print(f"Title: {book_info[0]}")
            print(f"Author: {book_info[1]}")

            confirm = input("Confirm deletion of this book? (y/n): ").lower()

            if confirm == 'y':
                c.execute("DELETE FROM book WHERE id = ?", (book_id,))
                conn.commit()
                print("Book deleted successfully!")
            else:
                print("Deletion cancelled.")
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")

def search_book():
    """Search book by title, author name or book ID
    including partial matches."""
    print("\n--- SEARCH BOOK ---")

    try:
        search_term = input("Enter search by title, author name or book ID: ").strip()
        if not search_term:
            print("Error: Search criteria must not be empty.")
            return
        
        with sqlite3.connect('ebookstore.db') as conn:
            c = conn.cursor()

            c.execute('''
                SELECT b.id, b.title, a.name, a.country, b.qty
                FROM book b
                JOIN author a ON b.authorID = a.id
                WHERE b.title LIKE ? COLLATE NOCASE
                  OR a.name LIKE ? COLLATE NOCASE
                  OR CAST(b.id AS TEXT) LIKE ?
            ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))

            results = c.fetchall()

            if not results:
                print("No books match the search criteria.")
                return
            
            print(f"\nFound {len(results)} book(s):")
            print("-" * 70)
            for book in results:
                print(f"ID: {book[0]}")
                print(f"Title: {book[1]}")
                print(f"Author: {book[2]} ({book[3]})")
                print(f"Quantity: {book[4]}")
                print("-" * 70)

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")

def view_all():
    """View all books with details in zip format."""
    print("\n--- VIEW ALL BOOKS ---")

    try:
        with sqlite3.connect('ebookstore.db') as conn:
            c = conn.cursor()

            # Fetch book titles
            c.execute('SELECT title FROM book ORDER BY title')
            titles = [row[0] for row in c.fetchall()]

            # Fetch author names
            c.execute('''
                SELECT a.name
                FROM book b
                JOIN author a ON b.authorID = a.id
                ORDER BY b.title
            ''')
            author_names = [row[0] for row in c.fetchall()]

            # Fetch author countries
            c.execute('''
                SELECT a.country
                FROM book b
                JOIN author a ON b.authorID = a.id
                ORDER BY b.title
            ''')
            countries = [row[0] for row in c.fetchall()]

            if not titles:
                print("No books found in the database.")
                return
            
            print("\nDetails " + "-" * 50)

            # Zip() the data together
            for title, author_name, country in zip(titles, author_names, countries):
                print(f"Title: {title}")
                print(f"Author's Name: {author_name}")
                print(f"Author's Country: {country}")
                print("-" * 60)

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")

def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("      SHELF TRACK - BOOKSTORE SYSTEM")
    print("=" * 40)
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("5. View details of all books")
    print("0. Exit")
    print("=" * 40)

def main():
    """Main program function."""
    print("Welcome to Shelf Track!")
    
    # Initialize database
    create_database()
    
    while True:
        try:
            display_menu()
            choice = input("Please select an option (0-5): ").strip()
            
            if choice == "0":
                print("Thank you for using Shelf Track. Goodbye!")
                break
            elif choice == "1":
                add_book()
            elif choice == "2":
                update_book()
            elif choice == "3":
                delete_book()
            elif choice == "4":
                search_book()
            elif choice == "5":
                view_all()
            else:
                print("Invalid choice. Please select a number between 0 and 5.")
            
            # Pause before showing menu again
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()