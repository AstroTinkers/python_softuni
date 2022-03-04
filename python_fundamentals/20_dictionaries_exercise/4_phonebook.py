contact = input()
phonebook = {}
while not contact.isnumeric():
    name, number = contact.split("-")
    entry = {name: number}
    phonebook.update(entry)
    contact = input()
for i in range(0, int(contact)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
