input_lines = int(input())
for line in range(input_lines):
    name_age = input()
    name = name_age[name_age.index("@") + 1:name_age.index("|")]
    age = name_age[name_age.index("#") + 1:name_age.index("*")]
    print(f"{name} is {age} years old.")
