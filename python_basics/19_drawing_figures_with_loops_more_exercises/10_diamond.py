diamond = int(input())
for n in range(int((diamond + 1)/2), 0, -1):
    print(f"{(n-1)*'-'}*{(diamond - (int(n-1)))*'-'}*{(n-1)*'-'}")