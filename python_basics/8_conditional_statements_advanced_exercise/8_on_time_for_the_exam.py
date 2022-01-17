exam_hour = int(input())
exam_min = int(input())
stud_hour = int(input())
stud_min = int(input())

exam_time = exam_hour * 60 + exam_min
stud_time = stud_hour * 60 + stud_min
difference = abs(exam_time - stud_time)
difference_h = difference // 60
difference_m = difference % 60
if exam_time == stud_time:
        print("On time")
elif exam_time > stud_time:
    if difference <= 30:
        print("On time")
        print(f"{difference} minutes before the start")
    elif difference < 60:
        print("Early")
        print(f"{difference_m} minutes before the start")
    elif difference >= 60:
        print("Early")
        print(f"{difference_h}:{difference_m:02d} hours before the start")
elif exam_time < stud_time:
    if difference < 60:
        print("Late")
        print(f"{difference_m} minutes after the start")
    elif difference >= 60:
        print("Late")
        print(f"{difference_h}:{difference_m:02d} hours after the start")