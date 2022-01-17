width = int(input())
length = int(input())
height = int(input())
volume = width * length * height
volume_full = False
finished = False
while not(volume_full or finished):
    boxes = input()
    if boxes == "Done":
        finished = True
    else:
        volume -= int(boxes)
        if volume < 0:
            volume_full = True
if volume_full:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")
if finished:
    print(f"{volume} Cubic meters left.")