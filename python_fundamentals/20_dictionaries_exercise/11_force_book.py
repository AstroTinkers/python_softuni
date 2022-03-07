def side_join(side, user, dict):
    dict.setdefault(side, [])
    user_not_in = True
    for key, value in dict.items():
        if user in value:
            user_not_in = False
    if user_not_in:
        dict[side].append(user)


def switch_side(side, user, dict):
    dict.setdefault(side, [])
    for value in dict.values():
        if user in value:
            value.remove(user)
    if user not in dict[side]:
        dict[side].append(user)


command = input()
force_users = {}
while command != "Lumpawaroo":
    if " | " in command:
        force_side, force_user = command.split(" | ")
        side_join(force_side, force_user, force_users)
    else:
        force_user, force_side = command.split(" -> ")
        switch_side(force_side, force_user, force_users)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for side, users in force_users.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
