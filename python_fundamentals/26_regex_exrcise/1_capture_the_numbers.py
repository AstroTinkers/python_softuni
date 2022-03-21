import re
pattern = r"\d+"
list_num = []
text = input()
while text != "":
    list_num += re.findall(pattern, text)
    text = input()
print(" ".join(list_num))
