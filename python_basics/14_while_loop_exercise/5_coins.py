resto = float(input())
coins = 0
resto = int(resto * 100)
while resto > 0:
    if resto // 200 > 0:
        coins += resto // 200
        resto = resto % 200
    elif resto // 100 > 0:
        coins += resto // 100
        resto = resto % 100
    elif resto // 50 > 0:
        coins += resto // 50
        resto = resto % 50
    elif resto // 20 > 0:
        coins += resto // 20
        resto = resto % 20
    elif resto // 10 > 0:
        coins += resto // 10
        resto = resto % 10
    elif resto // 5 > 0:
        coins += resto // 5
        resto = resto % 5
    elif resto // 2 > 0:
        coins += resto // 2
        resto = resto % 2
    elif resto // 1 > 0:
        coins += resto // 1
print(int(coins))