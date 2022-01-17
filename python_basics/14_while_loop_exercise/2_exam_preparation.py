bad_grades = int(input())
problem_name = input()
grade_sum = 0
problem_count = 0
last_problem = ""
bad_grade_count = 0
while problem_name != "Enough":
    grade = int(input())
    grade_sum += grade
    problem_count += 1
    last_problem = problem_name
    if grade <= 4:
        bad_grade_count += 1
        if bad_grade_count >= bad_grades:
            print(f"You need a break, {bad_grade_count} poor grades.")
            break
    problem_name = input()
else:
    average = grade_sum / problem_count
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {problem_count}")
    print(f"Last problem: {last_problem}")