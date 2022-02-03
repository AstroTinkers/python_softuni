first_line = [int(i) for i in input().split()]
second_line = [int(j) for j in input().split()]
third_line = [int(m) for m in input().split()]
winner = 0
for i in first_line:
    if first_line[i] == second_line[i] == third_line[i]:
        winner = first_line[i]
if all(j == first_line[0] for j in first_line):
    winner = first_line[0]
if all(k == second_line[0] for k in second_line):
    winner = second_line[0]
if all(l == third_line[0] for l in third_line):
    winner = third_line[0]
if first_line[0] == second_line[1] == third_line[2]:
    winner = first_line[0]
elif first_line[2] == second_line[1] == third_line[0]:
    winner = first_line[2]
if winner == 0:
    print("Draw!")
elif winner == 1:
    print("First player won")
else:
    print("Second player won")
