def factorial(number: int):
    result = number
    for i in range(number - 1, 0, -1):
        result = result * i
    return result


number_1, number_2 = int(input()), int(input())
final_result = factorial(number_1) / factorial(number_2)
print(f"{final_result:.2f}")
