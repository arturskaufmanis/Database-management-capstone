# Database-management-capstone
A Python bookstore management system demonstrating SQLite database operations, relational data modeling, and CRUD functionality with comprehensive validation and search capabilities.


## 📚 Shelf Track - Bookstore Management System

A Python-based bookstore inventory management application that demonstrates database operations, relational data modeling, and CRUD functionality using SQLite. This capstone project implements a practical bookstore system with comprehensive book and author management, search capabilities, and data validation features.

## 🎯 Project Overview

This bookstore management system provides functionality for managing book inventory and author information through a relational database structure. The application features SQLite database operations, foreign key relationships, comprehensive CRUD operations, and a user-friendly command-line interface for managing bookstore inventory with validation and error handling.

## ✨ Key Features

### 🗄️ Database Operations
- **SQLite Integration** - Implementation of embedded database with persistent storage
- **Relational Data Modeling** - Author and Book tables with foreign key relationships
- **CRUD Operations** - Complete Create, Read, Update, Delete functionality
- **Data Integrity** - Foreign key constraints and validation rules

### 📖 Book Management
- **Inventory Tracking** - Add, update, and delete book records
- **Author Association** - Link books to authors through relational database design
- **Quantity Management** - Track stock levels and inventory updates
- **Duplicate Prevention** - Validation to prevent duplicate book IDs

### 🔍 Search & Retrieval
- **Multi-Criteria Search** - Search by title, author name, or book ID
- **Partial Matching** - Case-insensitive substring search capabilities
- **Comprehensive Listing** - View all books with author details using ZIP operations
- **Relational Queries** - JOIN operations to combine book and author data

### 🛡️ Data Validation & Security
- **Input Validation** - Comprehensive validation for IDs, quantities, and text fields
- **Error Handling** - Robust exception management for database operations
- **Data Type Checking** - Validation of numeric inputs and data formats
- **Transaction Safety** - Safe database operations with rollback capabilities

## 🛠️ Technologies & Concepts Demonstrated

### Core Python Skills
- **Database Programming** - SQLite integration and SQL query execution
- **Object-Relational Operations** - Mapping database records to Python objects
- **File System Operations** - Database file creation and management
- **Exception Handling** - Comprehensive error management for database operations
- **Input/Output Processing** - User interaction and data presentation

### Database Concepts
- **Relational Database Design** - Primary keys, foreign keys, and table relationships
- **SQL Operations** - SELECT, INSERT, UPDATE, DELETE with JOIN operations
- **Data Normalization** - Proper separation of entities (books and authors)
- **Database Constraints** - Foreign key relationships and data integrity
- **Transaction Management** - Commit and rollback operations

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.6+** - Required for SQLite3 support and modern Python features
- **SQLite** - Built into Python standard library (no additional installation needed)

### Setup Instructions
```bash
# Download the project files
git clone <repository-url>
cd Database-Management-Capstone

# Run the application
python shelf_track.py
```

### File Structure
```
Database-Management-Capstone/
├── README.md
├── shelf_track.py           # Main application file
└── ebookstore.db           # SQLite database (created automatically)
```

## 📖 Usage Guide

### Starting the Application
```bash
python shelf_track.py
```

### Menu Options

| Option | Description | Functionality |
|--------|-------------|---------------|
| 1 | Enter book | Add new books to the inventory |
| 2 | Update book | Modify existing book or author information |
| 3 | Delete book | Remove books from the database |
| 4 | Search books | Find books by various criteria |
| 5 | View details of all books | Display complete inventory with ZIP operations |
| 0 | Exit | Close the application |

### Basic Operations

**Adding New Books:**
```
--- ADD NEW BOOK ---
Enter book ID (4 digits): 3006
Enter book title: The Hobbit
Enter author ID (4 digits): 6380
Enter quantity (positive integer): 20
Book 'The Hobbit' added successfully!
```

**Searching Books:**
```
--- SEARCH BOOK ---
Enter search by title, author name or book ID: Harry
Found 1 book(s):
----------------------------------------------------------------------
ID: 3002
Title: Harry Potter and the Philosopher's Stone
Author: J.K. Rowling (England)
Quantity: 40
----------------------------------------------------------------------
```

**Viewing All Books (ZIP Operation):**
```
--- VIEW ALL BOOKS ---
Details --------------------------------------------------
Title: A Tale of Two Cities
Author's Name: Charles Dickens
Author's Country: England
------------------------------------------------------------
Title: Alice's Adventures in Wonderland
Author's Name: Lewis Carroll
Author's Country: England
------------------------------------------------------------
```

## 🏗️ Database Architecture

### Table Structure
```sql
-- Author table
CREATE TABLE author (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT NOT NULL
);

-- Book table with foreign key relationship
CREATE TABLE book (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    authorID INTEGER NOT NULL,
    qty INTEGER NOT NULL,
    FOREIGN KEY (authorID) REFERENCES author(id)
);
```

### Core Functions
```python
def create_database():
    """Initialize SQLite database with tables and sample data"""
    
def add_book():
    """Add new book with author validation"""
    
def update_book():
    """Update book information with multiple options"""
    
def delete_book():
    """Remove book with confirmation"""
    
def search_book():
    """Search with partial matching and JOIN operations"""
    
def view_all():
    """Display all books using ZIP operations"""
```

### Validation Functions
```python
def validate_book_id(book_id):
    """Validate 4-digit book ID format"""
    
def validate_author_id(author_id):
    """Validate 4-digit author ID with existence check"""
    
def validate_quantity(qty):
    """Validate positive integer quantities"""
```

## 🎓 Programming Concepts Applied

### Database Programming
- **SQLite Integration** - Embedded database operations with Python
- **SQL Query Construction** - Dynamic query building with parameterized statements
- **JOIN Operations** - Combining data from multiple tables using relational operations
- **Transaction Management** - Safe database operations with commit/rollback functionality

### Data Structures & Operations
- **Relational Data Modeling** - Designing normalized database schema
- **Foreign Key Relationships** - Implementing referential integrity constraints
- **ZIP Operations** - Combining multiple data streams for display formatting
- **List Comprehensions** - Efficient data processing and transformation

### Input Validation & Error Handling
- **Data Type Validation** - Ensuring proper numeric and text input formats
- **Business Rule Enforcement** - Validating ID formats and existence checks
- **Exception Management** - Handling database errors and user input issues
- **User Experience** - Providing clear feedback and confirmation prompts

### Software Architecture
- **Modular Design** - Separation of concerns with focused functions
- **Database Abstraction** - Clean separation between UI and data operations
- **Error Recovery** - Graceful handling of database and user input errors
- **Menu-Driven Interface** - Structured user interaction with clear navigation

## 📈 Technical Features

### Database Operations
- **CRUD Functionality** - Complete Create, Read, Update, Delete operations
- **Relational Queries** - JOIN operations to combine author and book data
- **Data Integrity** - Foreign key constraints and validation rules
- **Parameterized Queries** - SQL injection prevention through prepared statements

### Search Capabilities
- **Multi-Field Search** - Search across title, author name, and book ID
- **Case-Insensitive Matching** - COLLATE NOCASE for flexible text searches
- **Partial String Matching** - LIKE operations with wildcard support
- **Result Formatting** - Professional display of search results

### Data Management
- **Automatic Initialization** - Database and table creation on first run
- **Sample Data Population** - Pre-loaded books and authors for testing
- **Data Validation** - Input sanitization and format checking
- **Error Prevention** - Duplicate checking and existence validation

## 🔧 Technical Specifications

### System Requirements
- **Python Version** - 3.6 or higher with SQLite3 support
- **Database** - SQLite (included with Python standard library)
- **Storage** - Local file-based database storage
- **Platform** - Cross-platform (Windows, macOS, Linux)

### Performance Characteristics
- **Database Size** - Suitable for small to medium bookstore inventories
- **Query Performance** - Indexed operations for efficient searching
- **Memory Usage** - Minimal memory footprint with SQLite
- **File Storage** - Efficient binary database format

### Data Integrity Features
- **Foreign Key Constraints** - Automatic referential integrity checking
- **Input Validation** - Multiple layers of data validation
- **Transaction Safety** - Atomic operations with rollback capabilities
- **Error Recovery** - Graceful handling of database corruption

## 🎯 Learning Outcomes

This project demonstrates understanding of:

- **Database Design** - Relational data modeling and normalization principles
- **SQL Operations** - Query construction, JOINs, and data manipulation
- **Python Database Programming** - SQLite integration and parameterized queries
- **Data Validation** - Input sanitization and business rule enforcement
- **Error Handling** - Comprehensive exception management for database operations
- **User Interface Design** - Menu-driven systems with clear user feedback

## 🚀 Potential Improvements

Areas for future development:

- **Advanced Search Filters** - Multiple criteria and date range searches
- **Reporting Features** - Generate inventory reports and statistics
- **Data Import/Export** - CSV import/export functionality
- **User Management** - Add user accounts and permission levels
- **Web Interface** - Flask/Django web application version
- **Backup System** - Automated database backup and restore features

## 📝 Development Notes

This project follows standard Python and database conventions:

- **PEP 8 Style Guide** - Consistent code formatting and naming conventions
- **SQL Best Practices** - Parameterized queries and proper indexing
- **Function Documentation** - Comprehensive docstrings for all functions
- **Error Handling** - Robust exception management throughout
- **Database Design** - Normalized schema with proper relationships

## 📄 Project Purpose

This project was created as a capstone demonstration of database programming, relational data modeling, and CRUD operations using Python and SQLite.
