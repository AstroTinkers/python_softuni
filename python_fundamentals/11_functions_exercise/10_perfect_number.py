def perfect_num(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number


input_num = int(input())
if perfect_num(input_num):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
