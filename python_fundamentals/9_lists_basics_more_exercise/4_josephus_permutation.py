people = input().split(" ")
number = int(input())
number_rotate = number - 1
kill_list = []
while len(people) > 0:
    if number_rotate < len(people):
        kill_list.append(people[number_rotate])
        people.pop(number_rotate)
        number_rotate += number - 1
    else:
        while number_rotate >= len(people):
            number_rotate -= len(people)
kill_list = list(map(int, kill_list))
print(f"{repr(kill_list).replace(' ', '')}")
