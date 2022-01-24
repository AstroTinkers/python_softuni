symbols = int(input())
final_sum = 0
for i in range(symbols):
    letter = input()
    final_sum += ord(letter)
print(f"The sum equals: {final_sum}")
