import re
pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b"
dates = input()
matches = re.findall(pattern, dates)
for i in matches:
    print(f"Day: {i[0]}, Month: {i[2]}, Year: {i[3]}")
