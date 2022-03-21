import re
pattern = r"\b_{1}([a-zA-Z0-1]+)\b"
input_text = input()
matched_ids = re.findall(pattern, input_text)
print(",".join(matched_ids))
