word_list = input().split()
repeat_list = []
for word in word_list:
    repeat_list.append(word * (len(word)))
final_list = "".join(repeat_list)
print(final_list)
