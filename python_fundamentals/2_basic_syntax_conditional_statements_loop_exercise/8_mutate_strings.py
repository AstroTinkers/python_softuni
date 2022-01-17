string_1 = input()
string_2 = input()

for i in range(len(string_1)):
    if string_1[i] != string_2[i]:
        string_1 = string_1[:i] + string_2[i] + string_1[i+1:]
        print(string_1)