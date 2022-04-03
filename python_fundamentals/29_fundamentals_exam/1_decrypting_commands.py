input_string = input()
command = input()
while not command == "Finish":
    command = command.split()
    if command[0] == "Replace":
        input_string = input_string.replace(command[1], command[2])
        print(input_string)
    elif command[0] == "Cut":
        command[1], command[2] = int(command[1]), int(command[2])
        if command[1] >= 0 and command[2] < len(input_string):
            input_string = input_string[:command[1]] + input_string[command[2] + 1:]
            print(input_string)
        else:
            print("Invalid indices!")
    elif command[0] == "Make":
        if command[1] == "Upper":
            input_string = input_string.upper()
            print(input_string)
        else:
            input_string = input_string.lower()
            print(input_string)
    elif command[0] == "Check":
        if command[1] in input_string:
            print(f"Message contains {command[1]}")
        else:
            print(f"Message doesn't contain {command[1]}")
    else:
        command[1], command[2] = int(command[1]), int(command[2])
        if command[1] >= 0 and command[2] < len(input_string):
            sum_ascii = 0
            iterable_string = input_string[command[1]:command[2]+1]
            for i in iterable_string:
                sum_ascii += ord(i)
            print(sum_ascii)
        else:
            print("Invalid indices!")
    command = input()
