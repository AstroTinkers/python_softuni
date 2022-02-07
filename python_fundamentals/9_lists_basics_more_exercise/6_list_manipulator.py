given_list = [int(i) for i in input().split()]
while True:
    command_line = input().split()
    if command_line[0] == "end":
        break
    else:
        if command_line[0] == "exchange":
            if int(command_line[1]) >= len(given_list) or int(command_line[1]) < 0:
                print("Invalid index")
            else:
                given_list = given_list[int(command_line[1]) + 1:] + given_list[:int(command_line[1]) + 1]
        elif command_line[0] == "max":
            if command_line[1] == "even":
                even_list = [i for i in given_list if i % 2 == 0]
                if even_list:
                    duplicates = [i for i, x in enumerate(given_list) if x == max(i for i in given_list if i % 2 == 0)]
                    print(duplicates[-1])
                else:
                    print("No matches")
            elif command_line[1] == "odd":
                odd_list = [i for i in given_list if i % 2 != 0]
                if odd_list:
                    duplicates = [i for i, x in enumerate(given_list) if x == max(i for i in given_list if i % 2 != 0)]
                    print(duplicates[-1])
                else:
                    print("No matches")
        elif command_line[0] == "min":
            if command_line[1] == "even":
                even_list = [i for i in given_list if i % 2 == 0]
                if even_list:
                    duplicates = [i for i, x in enumerate(given_list) if x == min(i for i in given_list if i % 2 == 0)]
                    print(duplicates[-1])
                else:
                    print("No matches")
            elif command_line[1] == "odd":
                odd_list = [i for i in given_list if i % 2 != 0]
                if odd_list:
                    duplicates = [i for i, x in enumerate(given_list) if x == min(i for i in given_list if i % 2 != 0)]
                    print(duplicates[-1])
                else:
                    print("No matches")
        elif command_line[0] == "first":
            if int(command_line[1]) > len(given_list):
                print("Invalid count")
            else:
                output = []
                empty = False
                if command_line[2] == "even":
                    for i in given_list:
                        if i % 2 == 0:
                            output.append(i)
                        if len(output) == int(command_line[1]):
                            print(output)
                            empty = True
                            break
                elif command_line[2] == "odd":
                    for i in given_list:
                        if i % 2 != 0:
                            output.append(i)
                        if len(output) == int(command_line[1]):
                            print(output)
                            empty = True
                            break
                if not empty:
                    print(output)
        elif command_line[0] == "last":
            if int(command_line[1]) > len(given_list):
                print("Invalid count")
            else:
                output = []
                empty = False
                if command_line[2] == "even":
                    for i in reversed(given_list):
                        if i % 2 == 0:
                            output.insert(0, i)
                        if len(output) == int(command_line[1]):
                            print(output)
                            empty = True
                            break
                elif command_line[2] == "odd":
                    for i in reversed(given_list):
                        if i % 2 != 0:
                            output.insert(0, i)
                        if len(output) == int(command_line[1]):
                            print(output)
                            empty = True
                            break
                if not empty:
                    print(output)
print(given_list)
