input_data = input()
students = {}
while ":" in input_data:
    name, id_num, course = input_data.split(":")
    students[id_num] = name, course
    input_data = input()
input_data = input_data.split("_")
input_data = " ".join(input_data)
for id_num, course in students.items():
    if input_data in course:
        print(f"{course[0]} - {id_num}")
