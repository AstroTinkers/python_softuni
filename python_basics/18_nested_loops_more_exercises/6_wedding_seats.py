last_sector = input()
rows_first_sector = int(input())
odd_row_seats = int(input())
seats = 0
for i in range(ord("A"), ord(last_sector) + 1):
    rows_first_sector += 1
    for j in range(1, rows_first_sector):
        if j % 2 == 0:
            for k in range(ord("a"), ord("a") + odd_row_seats + 2):
                print(f"{chr(i)}{j}{chr(k)}")
                seats += 1
        else:
            for k in range(ord("a"), ord("a") + odd_row_seats):
                print(f"{chr(i)}{j}{chr(k)}")
                seats += 1
print(seats)
