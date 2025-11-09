#Creating employee dataset
employees = [
    {"name": "María", "email": "maria@empresa.com", "department": "Marketing"},
    {"name": "Andrés", "email": "andres@empresa.com", "department": "TI"},
    {"name": "Paula", "email": "paula@empresa.com", "department": "Finanzas"},
    {"name": "Ricardo", "email": "ricardo@empresa.com", "department": "Marketing"},
    {"name": "Valeria", "email": "valeria@empresa.com", "department": "Soporte"},
    {"name": "Javier", "email": "javier@empresa.com", "department": "TI"},
]

# Empty dictionary that will store employees grouped by department
grouped = {}

# Loop through every employee in the list
for emp in employees:
    # setdefault() checks if the department already exists as a key in 'grouped'
    # If it does not exist, it creates it with an empty list []
    # Then, append() adds the current employee (emp) to that department's list
    grouped.setdefault(emp["department"], []).append(emp)

# Print the dictionary showing employees grouped by department
print(grouped)