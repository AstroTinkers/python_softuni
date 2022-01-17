jury = int(input())
average_presentation = 0
total_presentations = 0
average_course = 0
course_finished = False
while not course_finished:
    presentation_name = input()

    if presentation_name == "Finish":
        course_finished = True
        break
    total_presentations += 1
    for n in range(1, jury + 1):
        grade = float(input())
        average_presentation += grade

    average_presentation = average_presentation / jury
    print(f"{presentation_name} - {average_presentation:.2f}.")
    average_course += average_presentation
    average_presentation = 0

if course_finished:
    average_course = average_course / total_presentations
    print(f"Student's final assessment is {average_course:.2f}.")
