def get_student_data():
    """
    Get student information from user input
    Returns: tuple (name, matric_number, score)
    """
    name = input("Enter student name: ")
    matric = input("Enter matric number: ")
    score = float(input("Enter score (0-100): "))
    
    return name, matric, score
