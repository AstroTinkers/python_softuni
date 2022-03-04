words = int(input())
synonyms_dict = {}
for i in range(0, words):
    key = input()
    synonyms_dict.setdefault(key, [])
    synonyms_dict[key].append(input())
for key, value in synonyms_dict.items():
    print(f"{key} - {', '.join(value)}")
