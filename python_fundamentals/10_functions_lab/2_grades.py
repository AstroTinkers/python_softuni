def grade(a):
    if a < 3:
        return "Fail"
    elif a < 3.5:
        return "Poor"
    elif a < 4.5:
        return "Good"
    elif a < 5.5:
        return "Very Good"
    else:
        return "Excellent"


input_grade = float(input())
print(grade(input_grade))


