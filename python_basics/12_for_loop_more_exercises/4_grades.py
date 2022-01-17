students = int(input())
less_2 = 0
around_3 = 0
around_4 = 0
more_5 = 0
grade_avg = 0
for i in range(students):
    grade = float(input())
    if grade < 3:
        less_2 += 1
        grade_avg += grade
    elif grade < 4:
        around_3 += 1
        grade_avg += grade
    elif grade <= 4.99:
        around_4 += 1
        grade_avg += grade
    elif grade >= 5:
        more_5 += 1
        grade_avg += grade
avg_grade = grade_avg / students
top = (more_5 / students) * 100
a4 = (around_4 / students) * 100
a3 = (around_3 / students) * 100
bottom = (less_2 / students) * 100
print(f"Top students: {top:.2f}%")
print(f"Between 4.00 and 4.99: {a4:.2f}%")
print(f"Between 3.00 and 3.99: {a3:.2f}%")
print(f"Fail: {bottom:.2f}%")
print(f"Average: {avg_grade:.2f}")