input_string = input()
code = [chr(ord(i)+3) for i in input_string]
coded_string = "".join(code)
print(coded_string)
