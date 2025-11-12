employee = {
    "name": "Roberto", 
    "email": "robm@ecorp.com", 
    "access_level": 5, 
    "age": 32,
    }

list_of_keys = ["access_level", "age"]

#Popping each key and value in list
for key in list_of_keys:
    employee.pop(key) 

print(employee)