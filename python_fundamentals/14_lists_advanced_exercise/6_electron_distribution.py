electrons = int(input())
filled_shells = []
while electrons > 0:
    i = len(filled_shells) + 1
    electrons_gone = 2*(i**2)
    filled_shells.append(electrons_gone if electrons - electrons_gone >= 0 else electrons)
    electrons -= electrons_gone
print(filled_shells)
