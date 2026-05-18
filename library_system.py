import os
from datetime import datetime

FILE_NAME = "library_records.txt"


def create_file():
    """
    Create library_records.txt if it doesn't exist
    """
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as f:
            f.write("LIBRARY BORROWED BOOKS RECORDS\n")
            f.write("="*60 + "\n\n")
        print(f"File '{FILE_NAME}' created successfully!\n")


def add_book():
    """
    Add a new book record
    """
    title = input("Enter book title: ")
    borrower = input("Enter borrower name: ")
    date = input("Enter date borrowed (YYYY-MM-DD): ")
    
    record = f"Book: {title} | Borrower: {borrower} | Date: {date}\n"
    
    with open(FILE_NAME, 'a') as f:
        f.write(record)
    
    print("Book record added successfully!\n")


def display_records():
    """
    Display all saved records
    """
    if not os.path.exists(FILE_NAME):
        print("No records found. File doesn't exist yet.\n")
        return
    
    print("\n" + "="*60)
    print("ALL BORROWED BOOKS")
    print("="*60)
    
    with open(FILE_NAME, 'r') as f:
        content = f.read()
        print(content)


def count_books():
    """
    Count and display total books borrowed
    """
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return 0
    
    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()
    
    # Count lines with "Book:" keyword
    count = sum(1 for line in lines if line.startswith("Book:"))
    
    print(f"\nTotal books borrowed: {count}\n")
    return count


def main():
    """
    Main program for library system
    """
    create_file()
    
    while True:
        print("LIBRARY MANAGEMENT SYSTEM")
        print("1. Add book record")
        print("2. Display all records")
        print("3. Count total books")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            display_records()
        elif choice == '3':
            count_books()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
