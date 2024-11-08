from Student import Student
from Subject import Subject
from Term import Term
from Grades import Grade
from GradeTracker import GPATracker
from typing import Dict
import pickle

def input_student_details() -> Student:
    """Input the student’s name and ID and return a Student instance."""
    name = input("Enter student name: ")
    ID = input("Enter student ID: ")
    return Student(name, ID)

def add_term(gpa_tracker: GPATracker):
    """Add a new term with subjects and grades to the GPATracker instance."""
    gpa_tracker.add_term(create_term())

def create_term() -> Term:
    """Create and return a new Term instance based on inputted subjects and grades."""
    return Term(input_subjects())

def input_subjects() -> Dict[Subject, Grade]:
    number = int(input("Enter the number of subjects for this term: "))
    subjects = {}
    print("Enter subject details as 'credit hours, numeric grade' (e.g., '3,95'):")
def input_subjects() -> Dict[str, 'Grade']:  # Using string for Subject names as placeholders
    while True:
        try:
            number = int(input("Enter the number of subjects for this term: "))
            break
        except ValueError:
            print("Please enter a valid integer for the number of subjects.")
    
    subjects = {}
    print("Enter subject details as 'credit hours, numeric grade' (e.g., '3,95'):")

    for i in range(number):
        while True:
            try:
                subject_input = input(f"Enter details for subject {i + 1}: ")
                hrs, numeric_grade = subject_input.split(',')
                
                # Convert to integers and validate
                hrs = int(hrs.strip())
                numeric_grade = int(numeric_grade.strip())
                
                # Validate credit hours and grade values
                if hrs <= 0:
                    print("Credit hours should be a positive integer.")
                    continue
                if numeric_grade < 0 or numeric_grade > 100:
                    print("Numeric grade should be between 0 and 100.")
                    continue
                
                # Call a grade conversion function (example function provided)
                grade = get_grade(numeric_grade)
                subject_name = f"Subject {i + 1}"  # Placeholder name for simplicity
                
                # Assuming Subject and Grade are valid types
                subjects[subject_name] = grade
                break
            
            except ValueError:
                print("Invalid input format. Please enter details as 'credit hours, numeric grade'.")

    return subjects
    for i in range(number):
        while True:
            try:
                subject_input = input(f"Enter subject details for subject {i + 1}: ")
                hrs, numeric_grade = subject_input.split(',')
                hrs = int(hrs.strip())  # Convert credit hours to integer
                numeric_grade = int(numeric_grade.strip())  # Convert numeric grade to integer
                grade = get_grade(numeric_grade)
                subject_name = f"Subject {i + 1}"  # Placeholder subject name
                subjects[Subject(subject_name, hrs)] = grade
                break
            except ValueError:
                print("Invalid input format. Please enter the subject details as 'credit hours, numeric grade'.")

    return subjects

def get_grade(numeric_grade: int) -> Grade:
    """Convert a numeric grade to a Grade enumeration."""
    if numeric_grade >= 97:
        return Grade.A_plus
    elif numeric_grade >= 93:
        return Grade.A
    elif numeric_grade >= 89:
        return Grade.A_minus
    elif numeric_grade >= 84:
        return Grade.B_plus
    elif numeric_grade >= 80:
        return Grade.B
    elif numeric_grade >= 76:
        return Grade.B_minus
    elif numeric_grade >= 73:
        return Grade.C_plus
    elif numeric_grade >= 70:
        return Grade.C
    elif numeric_grade >= 67:
        return Grade.C_minus
    elif numeric_grade >= 64:
        return Grade.D_plus
    elif numeric_grade >= 60:
        return Grade.D
    else:
        return Grade.F

def load_data(filename: str):
    """Load GPA tracker data from a pickle file."""
    filename_extension = f"{filename}.pickle"
    try:
        with open(filename_extension, 'rb') as inp:
            return pickle.load(inp)
    except (FileNotFoundError, pickle.UnpicklingError) as ex:
        print("Student not found or unable to load data:", ex)
        return None

def old_new_student(student: Student) -> GPATracker:
    """Check if the student is old or new and return the appropriate GPATracker instance."""
    ans = input("Is this an old student? y/n: ")
    if ans.lower() == 'y':
        data = load_data(student.get_student_information())
        if data:
            return GPATracker(data)
        else:
            print("No previous data found; creating a new tracker.")
            return GPATracker(student)
    else:
        return GPATracker(student)

###---------------START---------------###
# Main execution
student = input_student_details()
gpa_tracker_1 = old_new_student(student)
add_term(gpa_tracker_1)

# Print student details to verify correct input and GPA calculations
if hasattr(gpa_tracker_1, 'print_student_details'):
    gpa_tracker_1.print_student_details()
else:
    print("Error: 'print_student_details' method not found in GPATracker class.")
