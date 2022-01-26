number = int(input())
isprime = True
for i in range(2, number):
    if number % i == 0:
        isprime = False
print(isprime)
