given_list = [int(i) for i in input().split()]
end = False


def exchange(a):
    new_list = given_list[a:] + given_list[:a]
    given_list = new_list
    return given_list


def max_min_index(a, b):
    output = ""
    if a == "max":
        if b == "even":
            output = given_list.index(max(i for i in given_list if i % 2 == 0))
        elif b == "odd":
            output = given_list.index(max(i for i in given_list if i % 2 != 0))
    elif a == "min":
        if b == "even":
            output = given_list.index(min(i for i in given_list if i % 2 == 0))
        elif b == "odd":
            output = given_list.index(min(i for i in given_list if i % 2 != 0))
    if output is None:
        return "No matches"
    else:
        return output


def firs_last_count(a, b, c):
    output = ""
    if int(b) > len(given_list):
        return "Invalid count"
    elif a == "first":
        if c == "even":
            output = []
            for i in range(0, len(given_list)):
                if given_list[i] % 2:
                    output.append(i)
                    if len(output) > b:
                        break
                else:
                    continue
        elif c == "odd":
            output = []
            while len(output) < b:
                for i in range(0, len(given_list)):
                    if not given_list[i] % 2:
                        output.append(i)
                        if len(output) > b:
                            break
                    else:
                        continue
    elif a == "last":
        if c == "even":
            output = []
            while len(output) < b:
                for i in range(len(given_list), -1, -1):
                    if given_list[i] % 2:
                        output.append(i)
                        if len(output) > b:
                            break
                    else:
                        continue
        elif c == "odd":
            output = []
            while len(output) < b:
                for i in range(len(given_list), -1, -1):
                    if not given_list[i] % 2:
                        output.append(i)
                        if len(output) > b:
                            break
                    else:
                        continue


def input_data():
    if command_line.startswith("exchange"):
        command_line.split(" ")
        exchange(int(command_line[1]))
    elif command_line.startswith("max" or "min"):
        command_line.split(" ")
        max_min_index(command_line[0], command_line[1])
    elif command_line.startswith("first" or "last"):
        command_line.split(" ")
        firs_last_count(command_line[0], command_line[1], command_line[2])

while not end:
    command_line = input()
    if command_line.startswith("end"):
        end = True
    else:
        input_data()
print(input_data())
