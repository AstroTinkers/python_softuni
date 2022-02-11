electrons = int(input())
filled_shells = []
while electrons > 0:
    i = len(filled_shells) + 1
    electrons_gone = 2*(i**2)
    if electrons - electrons_gone >= 0:
        filled_shells.append(electrons_gone)
    else:
        filled_shells.append(electrons)
    electrons -= electrons_gone
print(filled_shells)
