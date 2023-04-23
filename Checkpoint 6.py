import numpy as np

number_students = int(input("Enter the number of students: "))
number_subjects = int(input("Enter the number of subjects: "))

marks_array = np.zeros((number_students, number_subjects))

#Enter the marks of each student in each subject
for i in range(number_students):
    print(f"Enter the marks for student {i+1}:")
    for j in range(number_subjects):
        marks_array[i][j] = int(input(f"Subject {j+1}: "))

# Calculate the total marks for each student
total_marks = np.sum(marks_array, axis=1)

# Calculate the percentage for each student
percentage = (total_marks / (number_subjects * 100)) * 100

# Calculate the grade for each student
grades = np.where(percentage >= 90, "A+",
          np.where(percentage >= 80, "A",
          np.where(percentage >= 70, "B+",
          np.where(percentage >= 60, "B",
          np.where(percentage >= 50, "C", "F")))))

# Display the result for each student in a tabular format
print("\n")
print("{:<10} {:<10} {:<10} {:<10}".format("Student", "Total", "Percentage", "Grade"))
print("-" * 40)
for i in range(number_students):
    print("{:<10} {:<10} {:<10.2f} {:<10}".format(f"Student {i+1}", total_marks[i], percentage[i], grades[i]))

