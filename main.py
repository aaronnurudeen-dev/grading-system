import input_module
import logic_module
import output_module

def main():
    """
    Main program - process student records until user stops
    """
    while True:
        # Get student data
        name, matric, score = input_module.get_student_data()
        
        # Validate score
        if not logic_module.validate_score(score):
            print("Invalid score! Score must be between 0 and 100.\n")
            continue
        
        # Calculate grade
        grade = logic_module.calculate_grade(score)
        
        # Display result
        output_module.display_result(name, matric, score, grade)
        
        # Ask if user wants to continue
        cont = input("Add another student? (yes/no): ").lower()
        if cont != 'yes':
            print("Program ended!")
            break


if __name__ == "__main__":
    main()
