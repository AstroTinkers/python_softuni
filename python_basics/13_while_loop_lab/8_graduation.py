student = input()
grade = 0
fail = 0
grades = 0
grades_years = 0
while True:
    grades = float(input())
    if grades >= 4:
        grade += 1
        grades_years += grades
    elif grades < 4:
        fail += 1
    if fail > 1:
        grade += 1
        print(f"{student} has been excluded at {grade} grade")
        break
    elif grade == 12:
        average = grades_years / grade
        print(f"{student} graduated. Average grade: {average:.2f}")
        break
