total_people = 6
women_count = 0

for person_index in range(total_people):
    gender_input = input("Enter 1 = woman, 2 = man: ")
    if gender_input == "1":
        women_count += 1

percent_women = (women_count / total_people) * 100
percent_men = 100 - percent_women

print(f"{percent_women:.2f}% women")
print(f"{percent_men:.2f}% men")