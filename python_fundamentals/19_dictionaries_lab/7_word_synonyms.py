words = int(input())
synonyms_dict = {}
key = ""
for i in range(1, (words * 2) + 1):
    if i % 2 != 0:
        key = input()
    else:
        synonyms_dict.setdefault(key, [])
        synonyms_dict[key].append(input())
for key, value in synonyms_dict.items():
    print(f"{key} - {', '.join(value)}")
