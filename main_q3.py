from student_module import Student
import file_module


def main():
    """
    Main program for assignment submission system
    """
    while True:
        print("\nASSIGNMENT SUBMISSION SYSTEM")
        print("1. Add student submission")
        print("2. Display all records")
        print("3. Search student by matric number")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            # Accept student details
            name = input("Enter student name: ")
            matric = input("Enter matric number: ")
            course = input("Enter course code: ")
            
            # Create student object
            student = Student(name, matric, course)
            
            # Save to file
            file_module.save_student(student)
        
        elif choice == '2':
            # Display all records
            file_module.display_all_records()
        
        elif choice == '3':
            # Search by matric number
            matric = input("Enter matric number to search: ")
            file_module.search_by_matric(matric)
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
