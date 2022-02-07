def palindrome_check(number_list):
    for i in number_list:
        print(i == i[::-1])


list_of_nums = input().split(", ")
palindrome_check(list_of_nums)
