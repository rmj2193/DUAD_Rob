number_of_grades = int(input("Enter how many grades you will input: "))

approved_count = 0
disapproved_count = 0

total_sum = 0.0
approved_sum = 0.0
disapproved_sum = 0.0

for index in range(1, number_of_grades + 1):
    grade = float(input(f"Enter grade #{index} (0-100): "))
    total_sum += grade

    if grade >= 70:
        approved_count += 1
        approved_sum += grade
    elif grade < 70:
        disapproved_count += 1
        disapproved_sum += grade

overall_average = total_sum / number_of_grades

approved_average = approved_sum / approved_count if approved_count > 0 else None
disapproved_average = disapproved_sum / disapproved_count if disapproved_count > 0 else None

print(f"Approved count (>=70): {approved_count}")
print(f"Disapproved count (<70): {disapproved_count}")
print(f"Overall average: {overall_average:.2f}")

if approved_average is not None:
    print(f"Average of approved: {approved_average:.2f}")

if disapproved_average is not None:
    print(f"Average of disapproved: {disapproved_average:.2f}")
else:
    print("Average of disapproved: N/A (no grades < 70)")
