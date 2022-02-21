def command_shoot(index, power, target_list):
    target_list[index] -= power
    if target_list[index] <= 0:
        target_list.pop(index)
    return target_list


def command_add(index, value, target_list):
    target_list.insert(index, value)
    return target_list


def command_strike(index, radius, target_list):
    target_list = target_list[:index - radius] + target_list[index + radius + 1:]
    return target_list


target_sequence = [int(i) for i in input().split()]
command = input()
while not command == "End":
    command = command.split()
    command = command[0], int(command[1]), int(command[2])
    if command[0] == "Shoot" and 0 <= command[1] < len(target_sequence):
        target_sequence = command_shoot(command[1], command[2], target_sequence)
    elif command[0] == "Add":
        if 0 <= command[1] < len(target_sequence):
            target_sequence = command_add(command[1], command[2], target_sequence)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        if command[1] + command[2] < len(target_sequence) and command[1] - command[2] >= 0:
            target_sequence = command_strike(command[1], command[2], target_sequence)
        else:
            print("Strike missed!")
    command = input()
target_sequence = "|".join(str(i) for i in target_sequence)
print(target_sequence)
