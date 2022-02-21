phone_list = input().split(", ")
command = input()
while command != "End":
    word, phone = command.split(" - ")
    if word == "Add":
        if phone not in phone_list:
            phone_list.append(phone)
    if word == "Remove":
        if phone in phone_list:
            phone_list.remove(phone)
    if word == "Bonus phone":
        phone1, phone2 = phone.split(":")
        if phone1 in phone_list:
            phone_list.insert(phone_list.index(phone1) + 1, phone2)
    if word == "Last":
        if phone in phone_list:
            phone_list.remove(phone)
            phone_list.append(phone)
    command = input()
print(", ".join(phone_list))
