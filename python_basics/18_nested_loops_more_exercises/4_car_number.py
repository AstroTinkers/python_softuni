num_start = int(input())
num_end = int(input())

for i in range(num_start, num_end + 1):
    for k in range(num_start, num_end + 1):
        for m in range(num_start, num_end + 1):
            if (k + m) % 2 != 0:
                continue
            for j in range(num_start, num_end + 1):
                if i < j:
                    continue
                if i % 2 == 0 and j % 2 == 0:
                    continue
                if i % 2 != 0 and j % 2 != 0:
                    continue
                print(f"{i}{k}{m}{j}", end=" ")
