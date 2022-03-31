tour_stops = input()
tour_correction = input()
while not tour_correction == "Travel":
    tour_correction = tour_correction.split(":")
    if "Add" in tour_correction[0]:
        command, index, stop = tour_correction[0], tour_correction[1], tour_correction[2]
        index = int(index)
        if index < len(tour_stops):
            tour_stops = tour_stops[:index] + stop + tour_stops[index:]
        print(tour_stops)
    elif "Remove" in tour_correction[0]:
        command, start, stop = tour_correction[0], tour_correction[1], tour_correction[2]
        start, stop = int(start), int(stop)
        if start >= 0 and stop < len(tour_stops):
            tour_stops = tour_stops[0:start] + tour_stops[stop + 1:]
        print(tour_stops)
    else:
        command, old_string, new_string = tour_correction[0], tour_correction[1], tour_correction[2]
        if old_string in tour_stops:
            tour_stops = tour_stops.replace(old_string, new_string)
        print(tour_stops)
    tour_correction = input()
print(f"Ready for world tour! Planned stops: {tour_stops}")
