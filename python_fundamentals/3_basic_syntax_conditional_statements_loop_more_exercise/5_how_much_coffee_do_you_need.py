end = False
coffee = 0
while not end:
    event = input()
    if coffee > 5:
        print('You need extra sleep')
        break
    elif event == "END":
        end = True
        break
    elif event == "dog" or event == "cat" or event == "coding" or event == "movie":
        coffee += 1
    elif event == "DOG" or event == "CAT" or event == "CODING" or event == "MOVIE":
        coffee += 2
if coffee <= 5:
    print(coffee)