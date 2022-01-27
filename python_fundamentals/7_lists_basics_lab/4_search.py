lines = int(input())
key_word = input()
word_list = list()
for i in range(lines):
    word = input()
    word_list.append(word)
filtered_list = [j for j in word_list if key_word in j]
print(word_list)
print(filtered_list)
