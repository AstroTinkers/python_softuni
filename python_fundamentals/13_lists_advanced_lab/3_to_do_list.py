to_do_list = [0] * 10
while True:
    entry = input()
    if entry == "End":
        break
    else:
        entry = entry.split("-")
        to_do_list.pop(int(entry[0])-1)
        to_do_list.insert((int(entry[0])-1), entry[1])
to_do_list = [i for i in to_do_list if i != 0]
print(to_do_list)
