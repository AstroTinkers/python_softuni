student_tickets = 0
standard_tickets = 0
kid_tickets = 0
while not day_end:
    movie_name = input()
    if movie_name == "Finish":
        break

    free_seats = int(input())
    for ticket in range(free_seats + 1):
        if ticket == free_seats:
            hall_full_percent = (ticket / free_seats) * 100
            print(f"{movie_name} - {hall_full_percent:.2f}% full.")
            break
        ticket_type = input()
        if ticket_type == "End":
            hall_full_percent = (ticket / free_seats) * 100
            print(f"{movie_name} - {hall_full_percent:.2f}% full.")
            break

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

total_tickets = student_tickets + standard_tickets + kid_tickets
student_tickets_average = (student_tickets / total_tickets) * 100
standard_tickets_average = (standard_tickets / total_tickets) * 100
kid_tickets_average = (kid_tickets / total_tickets) * 100
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_average:.2f}% student tickets.")
print(f"{standard_tickets_average:.2f}% standard tickets.")
print(f"{kid_tickets_average:.2f}% kids tickets.")
