command = int(input())
students = {}
for data in range(command):
    name = input()
    grade = float(input())
    students.setdefault(name, [])
    students[name].append(grade)
for student, grades in students.items():
    if sum(grades) / len(grades) >= 4.50:
        print(f"{student} -> {sum(grades) / len(grades):.2f}")
