from actions import *
from data import *

def show_main_menu(students):
    while True:
        print("\n     === Main Menu ===")
        print("1. Enter Student information")
        print("2. View all student information")
        print("3. View top 3 Students average")
        print("4. View average grade for all students")
        print("5. View failed students")
        print("6. Delete student")
        print("7. Export all information to CSV")
        print("8. Import information from CSV")
        print("9. Exit")

        choice = input("Select an option (1-9): ").strip()
        # Option 1 to create a new student
        if choice == "1":
            enter_new_student(students)  
            pass
        # Option 2 to print all students
        elif choice == "2":
            print_students(students)
            pass
        #Option 3 to give us a top 3 students
        elif choice == "3":
            show_top_3_students(students)
            pass
        #Option 4 for to calculate the average of averages
        elif choice == "4":
            average_of_averages(students)
            pass
        #Option 5 for failed students
        elif choice == "5":
            show_failed_students(students)
            pass        
        #Option 6 to delete a student
        elif choice == "6":
            delete_student(students)
            pass    
        #Option 7 to export to CSV
        elif choice == "7":
            export_csv(students)
            pass
        #Option 8 to import from CSV
        elif choice == "8":
            import_students_from_csv(students)
            pass
        #Option 9 to exit menu
        elif choice == "9":
            print("Exiting program...")
            break
        else:
            print("Invalid option, please try again.")