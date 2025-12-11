from student import Student 

# Function to create student
def enter_new_student(students):
    full_name = validate_name()
    section = validate_section()

        # Check for duplicates before asking for grades
    if student_exists(students, full_name, section):
        print(
            f"\nA student with name '{full_name}' and section '{section}' "
            "already exists. Student was not added."
        )
        return

    spanish_grade = validate_grade("Spanish")
    english_grade = validate_grade("English")
    social_studies_grade = validate_grade("Social Studies")
    science_grade = validate_grade("Science")
    average_grade = calculate_average(spanish_grade, english_grade, social_studies_grade, science_grade)

    add_student(students, full_name, section, spanish_grade, english_grade, social_studies_grade, science_grade, average_grade)


#------------------------------------------------------------------------------------------------
# Validations for the name  
def validate_name():
    while True:
        full_name = input("Enter full name: ").strip()

        # Check if empty
        if not full_name:
            print("Name cannot be empty. Please try again.")
            continue

        # Check for numbers in the name
        if any(char.isdigit() for char in full_name):
            print("Name cannot contain numbers. Please try again.")
            continue

        # Name is valid
        return full_name
    
#------------------------------------------------------------------------------------------------    
# Validations for the section
def validate_section():
    while True:
        section = input("Enter section (e.g. 10A, 11B): ").strip().upper()

        # Empty check
        if not section:
            print("Section cannot be empty. Please try again.")
            continue

        # Must be at least 2 characters: some digits + 1 letter
        if len(section) < 2:
            print("Section must contain a grade number and a letter (e.g. 10A).")
            continue

        number_part = section[:-1]   # all except last char
        letter_part = section[-1]    # last char

        # Check that the first part is numeric
        if not number_part.isdigit():
            print("Section must start with a grade number (e.g. 10A).")
            continue

        # Check that the last char is a letter
        if not letter_part.isalpha():
            print("Section must end with a letter (e.g. 10A).")
            continue

        # Validate grade range
        grade = int(number_part)
        if grade < 1 or grade > 11:
            print("Grade must be between 1 and 11.")
            continue

        # If all checks pass, return the section
        return section
    
#------------------------------------------------------------------------------------------------    
# Validations for the grades
def validate_grade(subject_name):   
    while True:
        grade_input = input(f"Enter {subject_name} grade (0-100): ").strip()

        # Empty check
        if not grade_input:
            print("Grade cannot be empty. Please try again.")
            continue

        # Try to convert to number
        try:
            grade = float(grade_input)
        except ValueError:
            print("Grade must be a number. Please try again.")
            continue

        # Range check
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100. Please try again.")
            continue

        # If passed, the grade is valid
        return grade

#------------------------------------------------------------------------------------------------    
# Calculation for average grade (works for n number of grades)
def calculate_average(*grades):

    if not grades:
        return 0.0  #Return 0 if no parameters/grades

    total = 0
    count = 0

    for grade in grades:
        total += grade
        count += 1

    return total / count

#------------------------------------------------------------------------------------------------    
# Create object and append to students
def add_student(students, full_name, section, spanish_grade, english_grade, social_studies_grade, science_grade, average_grade):
    student = Student(
        full_name,
        section,
        spanish_grade,
        english_grade,
        social_studies_grade,
        science_grade,
        average_grade
    )
    students.append(student)

#------------------------------------------------------------------------------------------------    
# Print student

def print_student(student):
    print("")
    print(f"Name: {student.full_name}")
    print(f"Section: {student.full_name}")
    print(f"Spanish grade: {student.spanish_grade}")
    print(f"English grade: {student.english_grade}")
    print(f"Social Studies grade: {student.social_studies_grade}")
    print(f"Science grade: {student.science_grade}")
    print(f"Average grade: {student.average_grade:.2f}")

#------------------------------------------------------------------------------------------------    
# Print students
def print_students(students):
    if not students:
        print("No students have been added yet")
    else:
        for student in students:
            print_student(student)

#------------------------------------------------------------------------------------------------    
# Print students average of averages

def average_of_averages(students):
    if not students:
        print("No students available to calculate average.")
    else:            
        averages = []
        for student in students:
            averages.append(student.average_grade)
        overall_average = calculate_average(*averages)
        print(f"Average grade for all students: {overall_average:.2f}")

#------------------------------------------------------------------------------------------------    
# Print students with top 3 grades

def show_top_3_students(students):
    if not students:
        print("No students available to calculate top 3.")
        return

    # Get all distinct averages
    distinct_averages = {student.average_grade for student in students}

    # Sort them from highest to lowest
    sorted_averages = sorted(distinct_averages, reverse=True)

    # Take the top 3 distinct averages **learned :3**
    top_3_averages = sorted_averages[:3]

    # Filter students whose average is in the top 3 averages
    top_students = [
        student for student in students
        if student.average_grade in top_3_averages
    ]

    # Sort those students by average **learned lambda usage**
    top_students.sort(
        key=lambda s: (s.average_grade, s.full_name),
        reverse=True
    )

    print("\n***Top students (top 3 distinct averages)***")
    print(f"Distinct averages considered: {', '.join(f'{avg:.2f}' for avg in top_3_averages)}")

    #Learned enumerate**
    for position, student in enumerate(top_students, start=1):
        print(f"\n#{position}")
        print_student(student)

#------------------------------------------------------------------------------------------------    
# Validate for duplicate students
def student_exists(students, full_name, section):
    for student in students:
        same_name = student.full_name.lower() == full_name.lower() # Compare names
        same_section = student.section.upper() == section.upper() # Compare sections

        if same_name and same_section:
            return True

    return False

#------------------------------------------------------------------------------------------------    
# Show failed students (any subject < 60)

def show_failed_students(students):
    if not students:
        print("No students available to check for failed subjects.")
        return

    failed_any = False

    for student in students:
        failed_subjects = []

        if student.spanish_grade < 60:
            failed_subjects.append(("Spanish", student.spanish_grade))
        if student.english_grade < 60:
            failed_subjects.append(("English", student.english_grade))
        if student.social_studies_grade < 60:
            failed_subjects.append(("Social Studies", student.social_studies_grade))
        if student.science_grade < 60:
            failed_subjects.append(("Science", student.science_grade))

        if failed_subjects:
            failed_any = True
            print("\n*** Failed student ***")
            print(f"Name: {student.full_name}")
            print(f"Section: {student.full_name}")
            print("Failed subjects:")
            for subject, grade in failed_subjects:
                print(f"  - {subject}: {grade}")

    if not failed_any:
        print("No failed students. All students passed all subjects.")

#------------------------------------------------------------------------------------------------    
# Delete a student by name and section

def delete_student(students):
    if not students:
        print("There are no students to delete.")
        return

    print("\n=== Delete student ===")
    full_name = validate_name()
    section = validate_section()

    index_to_delete = None

    for index, student in enumerate(students):
        same_name = student.full_name.lower() == full_name.lower()
        same_section = student.section.upper() == section.upper()

        if same_name and same_section:
            index_to_delete = index
            break

    if index_to_delete is None:
        print(f"No student found with name '{full_name}' in section '{section}'.")
        return

    print("\nStudent found:")
    print_student(students[index_to_delete])

    confirm = input("\nAre you sure you want to delete this student? (Y/N): ").strip().upper()
    if confirm == "Y":
        deleted_student = students.pop(index_to_delete)
        print(
            f"Student '{deleted_student.full_name}' "
            f"from section '{deleted_student.full_name}' deleted successfully."
        )
    else:
        print("Deletion canceled.")