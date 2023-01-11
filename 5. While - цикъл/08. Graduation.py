name = input()
grade = float(input())
bad_grades = 0
student_class = 1
average_grade = 0

while True:
    if grade < 4:
        bad_grades += 1
        if bad_grades == 2:
            print(f"{name} has been excluded at {student_class} grade")
            break
        grade = float(input())

    average_grade = grade + average_grade

    if student_class == 12:
        print(f"{name} graduated. Average grade: {average_grade / 12:.2f}")
        break

    elif grade >= 4:
        student_class += 1
        grade = float(input())

