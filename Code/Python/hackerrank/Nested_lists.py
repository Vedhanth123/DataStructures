# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

nested_list = [['Harry', 37.21], ['Berry', 37.21], [
    'Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

# finding the second highest value
marks_of_student = []

for x in range(len(nested_list)):
    
    marks_of_student.append(nested_list[x][1])

marks_of_student.sort()

second_lowest_marks_of_student = 0

for x in marks_of_student:
    if(marks_of_student[0] < x):
        second_lowest_marks_of_student = x
        break


print(marks_of_student)

final_students = []

for x in range(len(marks_of_student)):

    if(second_lowest_marks_of_student == nested_list[x][1]):

        final_students.append(nested_list[x][0])

final_students.sort()

print(final_students)