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
        
        choice = input("Choose option (1-4): ").strip()
        
        if choice == '1':
            # Get student details
            name = input("Enter student name: ")
            matric = input("Enter matric number: ")
            course = input("Enter course code: ")
            
            # Create student object and save
            student = Student(name, matric, course)
            file_module.save_student_record(student)
        
        elif choice == '2':
            file_module.display_all_records()
        
        elif choice == '3':
            matric = input("Enter matric number to search: ")
            student = file_module.search_by_matric(matric)
            
            if student:
                print("\n" + "="*60)
                print("STUDENT FOUND")
                print("="*60)
                print(student)
                print("="*60 + "\n")
            else:
                print("Student not found!\n")
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
