num = int(input())
bonus = 0
if num < 100:
    bonus += 5
elif 100 < num <+ 1000:
    bonus += num * 0.2
else:
    bonus += num * 0.1

if num % 2 == 0:
    bonus += 1
if num % 10 == 5:
    bonus += 2

final = num + bonus

print(bonus)
print(final)