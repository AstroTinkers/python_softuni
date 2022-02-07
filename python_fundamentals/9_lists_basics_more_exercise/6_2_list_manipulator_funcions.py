def exchange(index, list):
    if index > len(list) or index < 0:
        print("Invalid index")
        return list
    else:
        return list[index + 1:] + list[:index + 1]


def max_index(command, list):
    if command == "even":
        even_list = [i for i in list if i % 2 == 0]
        if even_list:
            return list.index(max(i for i in list if i % 2 == 0))
        else:
            return "No matches"
    elif command == "odd":
        odd_list = [i for i in list if i % 2 != 0]
        if odd_list:
            return list.index(max(i for i in list if i % 2 != 0))
        else:
            return "No matches"


def min_index(command, list):
    if command == "even":
        even_list = [i for i in list if i % 2 == 0]
        if even_list:
            return list.index(min(i for i in list if i % 2 == 0))
        else:
            return "No matches"
    elif command == "odd":
        odd_list = [i for i in list if i % 2 != 0]
        if odd_list:
            return list.index(min(i for i in list if i % 2 != 0))
        else:
            return "No matches"


def first_count(index, command, list):
    if index > len(list):
        return "Invalid count"
    else:
        output = []
        if command == "even":
            for i in list:
                if i % 2 == 0:
                    output.append(i)
                    if len(output) == index:
                        return output
            return output
        elif command == "odd":
            for i in list:
                if i % 2 != 0:
                    output.append(i)
                    if len(output) == index:
                        return output
            return output


def last_count(index, command, list):
    if int(index) > len(list):
        print("Invalid count")
    else:
        output = []
        if command == "even":
            for i in reversed(list):
                if i % 2 == 0:
                    output.append(i)
                    if len(output) == index:
                        return output
            return output
        elif command == "odd":
            for i in reversed(list):
                if i % 2 != 0:
                    output.append(i)
                    if len(output) == index:
                        return output
            return output


given_list = [int(i) for i in input().split()]
while True:
    command_line = input().split()
    if command_line[0] == "end":
        break
    else:
        if command_line[0] == "exchange":
            given_list = exchange(int(command_line[1]), given_list)
        elif command_line[0] == "max":
            print(max_index(command_line[1], given_list))
        elif command_line[0] == "min":
            print(min_index(command_line[1], given_list))
        elif command_line[0] == "first":
            print(first_count(int(command_line[1]), command_line[2], given_list))
        elif command_line[0] == "last":
            print(last_count(int(command_line[1]), command_line[2], given_list))
print(given_list)
