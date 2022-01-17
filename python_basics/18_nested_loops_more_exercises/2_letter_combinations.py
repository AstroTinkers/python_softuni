start = input()
end = input()
blacklist = input()
counter = 0
for i in range(ord(start), ord(end) + 1):
    if i == ord(blacklist):
        continue
    for j in range(ord(start), ord(end) + 1):
        if j == ord(blacklist):
            continue
        for k in range(ord(start), ord(end) + 1):
            if k == ord(blacklist):
                continue
            counter += 1
            print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")
print(counter)
