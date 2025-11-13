# Initialize data structures
students = {}  # Dictionary to store student info
subjects = set()  # Set to store all unique subjects

# Function to add a student
def add_student():
    name = input("Enter student's name: ")
    roll_number = input("Enter roll number: ")
    
    # Check if the student already exists
    if roll_number in students:
        print(f"Student with roll number {roll_number} already exists.")
        return
    
    # Get subjects for the student
    student_subjects = input("Enter subjects separated by commas: ").split(',')
    print("student_subjects",student_subjects)
    student_subjects = [subject.strip() for subject in student_subjects]
    
    # Store student info in the dictionary
    students[roll_number] = {"name": name, "subjects": student_subjects}
    
    # Add subjects to the set
    for subject in student_subjects:
        subjects.add(subject)
    
    print(f"Student {name} with roll number {roll_number} added successfully.")

# Function to update student's subjects
def update_student_subjects():
    roll_number = input("Enter the roll number of the student to update: ")
    
    # Check if the student exists
    if roll_number not in students:
        print(f"No student found with roll number {roll_number}.")
        return
    
    # Get the new subjects
    student_subjects = input("Enter new subjects separated by commas: ").split(',')
    student_subjects = [subject.strip() for subject in student_subjects]
    
    # Update the subjects of the student
    students[roll_number]["subjects"] = student_subjects
    
    # Update the set of unique subjects
    for subject in student_subjects:
        subjects.add(subject)
    
    print(f"Subjects for student {students[roll_number]['name']} updated successfully.")

# Function to remove a student
def remove_student():
    roll_number = input("Enter the roll number of the student to remove: ")
    
    if roll_number not in students:
        print(f"No student found with roll number {roll_number}.")
        return
    
    # Remove the student from the dictionary
    student_name = students[roll_number]["name"]
    del students[roll_number]
    
    print(f"Student {student_name} with roll number {roll_number} removed successfully.")

# Function to display all students
def display_students():
    if not students:
        print("No students in the system.")
        return
    
    for roll_number, student_info in students.items():
        name = student_info["name"]
        subjects = ', '.join(student_info["subjects"])
        print(f"Roll Number: {roll_number}, Name: {name}, Subjects: {subjects}")

# Function to display unique subjects
def display_unique_subjects():
    if not subjects:
        print("No subjects available.")
        return
    
    print("Unique subjects offered:")
    for subject in sorted(subjects):
        print(subject)

# Function to display students enrolled in a specific subject
def display_students_in_subject():
    subject = input("Enter the subject to view students: ")
    
    enrolled_students = []
    for student_info in students.values():
        if subject in student_info["subjects"]:
            enrolled_students.append(student_info["name"])
    
    if enrolled_students:
        print(f"Students enrolled in {subject}:")
        for student in enrolled_students:
            print(student)
    else:
        print(f"No students are enrolled in {subject}.")

# Main function to run the program
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Update Student Subjects")
        print("3. Remove Student")
        print("4. Display All Students")
        print("5. Display Unique Subjects")
        print("6. Display Students in a Subject")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            update_student_subjects()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            display_students()
        elif choice == '5':
            display_unique_subjects()
        elif choice == '6':
            display_students_in_subject()
        elif choice == '7':
            print("Exiting the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
