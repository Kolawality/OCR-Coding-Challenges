import time
import csv
from Arithmetic_test_classes import StudentQuiz


# Introduce the program a
print()
print("********************************************")
print()
print("It's time for the test")
print()
print("********************************************")
print()

# Ask the user for their name and class
student_name = input("Please enter your first name: ")
student_class = input("Enter your class: ")

time.sleep(1)
print()
print()

# Creates a student object using their name and class
student_name = StudentQuiz(student_name, student_class)

# The new student (student object) takes the test
student_name.student_entry()

# In the csv file list the name and student, with their three results in
# order of highest to lowest
with open('student scores.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        all_scores = [line[2], line[3], line[4]]
        all_scores.sort(reverse=True)
        print("{0:^10} {1:^10} {2:^10} {3:^10} {4:^10}"
              .format(line[0], line[1], all_scores[0], all_scores[1],
                      all_scores[2]))

