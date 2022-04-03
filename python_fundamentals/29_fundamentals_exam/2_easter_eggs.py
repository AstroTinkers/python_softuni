import re

input_string = input()
pattern = r"(@|#)+(?P<color>[a-z]{3,})(@|#)+([^a-zA-Z0-9]+)?/+(?P<number>\d+)/+"
matches = re.finditer(pattern, input_string)
for match in matches:
    print(f"You found {match.group('number')} {match.group('color')} eggs!")
