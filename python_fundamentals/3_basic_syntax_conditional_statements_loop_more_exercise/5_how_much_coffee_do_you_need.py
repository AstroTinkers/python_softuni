end = False
coffee = 0
while not end:
    event = input()
    if coffee > 5:
        print('You need extra sleep')
        break
    if event == "END":
        end = True
        break
    elif event == "dog":
        coffee += 1
    elif event == "DOG":
        coffee += 2
    elif event == "cat":
        coffee += 1
    elif event == "CAT":
        coffee += 2
    elif event == "coding":
        coffee += 1
    elif event == "CODING":
        coffee += 2
    elif event == "movie":
        coffee += 1
    elif event == "MOVIE":
        coffee += 2
if coffee < 5:
    print(coffee)