bad_grades = int(input())
name_of_exercise = input()
grade = int(input())
bad_grade_counter = 0
average_grade = 0
grade_counter = 0
last_problem = ''

while name_of_exercise != "Enough":
    if grade <= 4:
        bad_grade_counter += 1
        grade_counter += 1
        average_grade = grade + average_grade
    elif grade > 4:
        average_grade = grade + average_grade
        grade_counter += 1

    if bad_grade_counter == bad_grades:
        print(f"You need a break, {bad_grade_counter} poor grades.")
        break
    last_problem = name_of_exercise
    name_of_exercise = input()
    if name_of_exercise == "Enough":
        break
    grade = int(input())

if name_of_exercise == "Enough":
    print(f"Average score: {average_grade / grade_counter:.2f}")
    print(f"Number of problems: {grade_counter}")
    print(f"Last problem: {last_problem}")