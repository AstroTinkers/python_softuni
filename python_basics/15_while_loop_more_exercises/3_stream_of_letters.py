c = 0
n = 0
o = 0
word = ""
word_read = ""
stop = False
letter = input()
while letter != "End":
    if letter.isalpha():
        if letter == "n":
            if n < 1:
                n = 1
            else:
                word += letter
        elif letter == "c":
            if c < 1:
                c = 1
            else:
                word += letter
        elif letter == "o":
            if o < 1:
                o = 1
            else:
                word += letter
        elif letter != ("n", "c", "o"):
            word += letter
    if o == 1 and n == 1 and c == 1:
        word_read += " "
        word_read += word
        word = ""
        o = 0
        n = 0
        c = 0
    letter = input()
else:
    print(word_read)