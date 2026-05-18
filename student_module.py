class Student:
    """
    Student class to store student information
    """
    def __init__(self, name, matric_number, course_code):
        self.name = name
        self.matric_number = matric_number
        self.course_code = course_code
    
    def __str__(self):
        """
        String representation of student
        """
        return f"{self.name} | Matric: {self.matric_number} | Course: {self.course_code}"
    
    def to_file_format(self):
        """
        Format student data for file storage
        """
        return f"{self.name},{self.matric_number},{self.course_code}\n"
