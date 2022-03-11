explosion_text = input()
new_string = ""
explosion_power = 0
index_pos = 0
while index_pos < len(explosion_text):
    current_element = explosion_text[index_pos]
    explosion_power = max(0, explosion_power - 1)

    if current_element == ">":
        explosion_power += int(explosion_text[index_pos + 1])
        new_string += current_element
        index_pos += 2
        continue

    if explosion_power == 0:
        new_string += explosion_text[index_pos]
        index_pos += 1
        continue
    index_pos += 1
print(new_string)
