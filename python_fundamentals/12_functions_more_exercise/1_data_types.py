def type_of_data(command, input_data):
    if command == "int":
        return int(input_data) * 2
    if command == "real":
        return f"{float(input_data) * 1.5:.2f}"
    if command == "string":
        return f"${input_data}$"


command_word = input()
data = input()
print(type_of_data(command_word, data))
