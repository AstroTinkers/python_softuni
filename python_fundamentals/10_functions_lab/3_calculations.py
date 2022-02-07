def calculator(word, num1, num2):
    if word == "multiply":
        return num1 * num2
    elif word == "divide":
        return num1 / num2
    elif word == "add":
        return num1 + num2
    else:
        return num1 - num2


command, number_1, number_2 = input(), int(input()), int(input())
print(int(calculator(command, number_1, number_2)))
