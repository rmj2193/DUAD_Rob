list_a = ["first_name", "last_name", "role"]
list_b = ["Rob", "Monge", "HR Specialist II"]

my_dict = {}

#Creating keys and values
for index in range(len(list_a)):
    key = list_a[index]
    value = list_b[index]
    my_dict[key] = value

print(my_dict)