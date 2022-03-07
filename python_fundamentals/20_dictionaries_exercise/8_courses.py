command = input()
courses = {}
while command != "end":
    course, name = command.split(" : ")
    courses.setdefault(course, [])
    courses[course].append(name)
    command = input()
for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
