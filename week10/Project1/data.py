import csv
import os

# Export to CSV 
def export_csv(students, filename="students.csv"):
    if not students:
        print("There are no students to export.")
        return

    # These must match the keys you use in your student dictionary
    fieldnames = [
        "full_name",
        "section",
        "spanish_grade",
        "english_grade",
        "social_studies_grade",
        "science_grade",
        "average_grade"
    ]

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write header row
            writer.writeheader()

            # Write one row per student
            for student in students:
                writer.writerow(student)

        print(f"Data exported successfully to '{filename}'.")
    except OSError as error:
        print(f"Error exporting data: {error}")


# Import from CSV

def import_students_from_csv(students, filename="students.csv"):
    if not os.path.exists(filename): # Existence Validation
        print(f"No exported data file found ('{filename}'). Please export data first.")
        return
    
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            rows = list(reader)
            if not rows:
                print(f"The file '{filename}' is empty. No data to import.")
                return

            # Clear current data to avoid duplicates
            students.clear()

            for row in rows:
                try:
                    student = {
                        "full_name": row["full_name"],
                        "section": row["section"],
                        "spanish_grade": float(row["spanish_grade"]),
                        "english_grade": float(row["english_grade"]),
                        "social_studies_grade": float(row["social_studies_grade"]),
                        "science_grade": float(row["science_grade"]),
                        "average_grade": float(row["average_grade"]),
                    }
                except (KeyError, ValueError) as error:
                    print(f"Skipping invalid row in CSV: {row} ({error})")
                    continue

                students.append(student)

        print(f"Data imported successfully from '{filename}'.")
        print(f"Total students loaded: {len(students)}")
    except OSError as error:
        print(f"Error reading file '{filename}': {error}")