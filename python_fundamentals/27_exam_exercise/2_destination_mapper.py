import re
pattern = r"(=|\/)([A-Z][a-zA-Z]{2,})\1"
input_data = input()
matches = re.findall(pattern, input_data)
matched_string = [match[1] for match in matches]
travel_points = len("".join(matched_string))
print(f"Destinations: {', '.join(matched_string)}\nTravel Points: {travel_points}")
