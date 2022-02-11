input_list = input().split(" ")
palindrome = input()
palindrome_list = []
palindrome_counter = 0
for i in input_list:
    j = [j for j in i]
    m = [m for m in i]
    m.reverse()
    if m == j:
        palindrome_list.append(i)
    if i == palindrome:
        palindrome_counter += 1
print(palindrome_list)
print(f"Found palindrome {palindrome_counter} times")
