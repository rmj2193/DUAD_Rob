# student.py

class Student:
    def __init__(self, full_name, section, spanish_grade, english_grade, social_studies_grade, science_grade, average_grade):
        self.full_name = full_name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_studies_grade = social_studies_grade
        self.science_grade = science_grade
        self.average_grade = average_grade

    def to_dictionary(self):
        #Convert object → dict (used for CSV export)
        return {
            "full_name": self.full_name,
            "section": self.section,
            "spanish_grade": self.spanish_grade,
            "english_grade": self.english_grade,
            "social_studies_grade": self.social_studies_grade,
            "science_grade": self.science_grade,
            "average_grade": self.average_grade
        }

    def from_dictionary(data):
        #Convert dict → Student (used for CSV import).
        return Student(
            data["full_name"],
            data["section"],
            float(data["spanish_grade"]),
            float(data["english_grade"]),
            float(data["social_studies_grade"]),
            float(data["science_grade"]),
            float(data["average_grade"])
        )
