speed = float(input())
if speed <= 10:
    print("slow")
elif 10 < speed and speed <= 50:
    print("average")
elif 50 < speed and speed <= 150:
    print("fast")
elif 150 < speed and speed <= 1000:
    print("ultra fast")
else:
    print("extremely fast")