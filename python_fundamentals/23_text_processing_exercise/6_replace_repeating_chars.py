input_string = input()
check = ""
no_duplicates_list = ""
for i in range(len(input_string)):
    if input_string[i] == check:
        pass
    else:
        check = input_string[i]
        no_duplicates_list += check
print(no_duplicates_list)
