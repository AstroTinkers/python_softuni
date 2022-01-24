people = int(input())
capacity = int(input())
courses = 0
courses += people // capacity
if people % capacity > 0:
    courses += 1
print(courses)
