import os
from student_module import Student

FILE_NAME = "submissions.txt"


def create_file():
    """
    Create submissions.txt if it doesn't exist
    """
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as f:
            f.write("ASSIGNMENT SUBMISSIONS\n")
            f.write("="*60 + "\n\n")


def save_student(student):
    """
    Save student record to file
    """
    create_file()
    
    with open(FILE_NAME, 'a') as f:
        f.write(student.to_file_format())
    
    print("Student record saved successfully!\n")


def display_all_records():
    """
    Display all submitted records
    """
    if not os.path.exists(FILE_NAME):
        print("No records found yet.\n")
        return
    
    print("\n" + "="*60)
    print("ALL SUBMITTED RECORDS")
    print("="*60)
    
    with open(FILE_NAME, 'r') as f:
        content = f.read()
        print(content)


def search_by_matric(matric_number):
    """
    Search for a student using matric number
    """
    if not os.path.exists(FILE_NAME):
        print("No records found yet.\n")
        return None
    
    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if ',' in line:  # Skip header lines
            parts = line.strip().split(',')
            if len(parts) >= 2 and parts[1] == matric_number:
                print(f"\nStudent Found!")
                print(f"Name: {parts[0]}")
                print(f"Matric: {parts[1]}")
                print(f"Course: {parts[2] if len(parts) > 2 else 'N/A'}\n")
                return parts
    
    print(f"No student found with matric number: {matric_number}\n")
    return None
