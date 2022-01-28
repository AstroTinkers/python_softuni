int_list = input()
count_remove = int(input())
list_final = int_list.split(" ")
list_arranged = sorted(list_final, key=lambda number: (number.isnumeric(), int(number)))
for i in range(count_remove):
    list_arranged.pop(0)
list_final = [i for i in list_final if i in list_arranged]
list_final = ", ".join([str(number) for number in list_final])
print(list_final)
