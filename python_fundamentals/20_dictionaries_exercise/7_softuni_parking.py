def register(username, licence_plate, listing):
    if username in listing:
        return f"ERROR: already registered with plate number {listing[username]}"
    else:
        listing[username] = licence_plate
        return f"{username} registered {licence_plate} successfully"


def unregister(username, listing):
    if username not in listing:
        return f"ERROR: user {username} not found"
    else:
        listing.pop(username)
        return f"{username} unregistered successfully"


commands = int(input())
parking_list = {}
for line in range(commands):
    input_data = input().split(" ")
    if input_data[0] == "register":
        print(register(input_data[1], input_data[2], parking_list))
    elif input_data[0] == "unregister":
        print(unregister(input_data[1], parking_list))
for user, plate in parking_list.items():
    print(f"{user} => {plate}")
