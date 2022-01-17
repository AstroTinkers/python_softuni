expected_sum = int(input())
sum_gathered = False
event_end = False
money_cash = 0
money_card = 0
counter_cash = 0
counter_card = 0
counter = 0
transaction = input()
while not(sum_gathered and event_end):
    if transaction == "End":
        event_end = True
        break
    else:
        transaction = int(transaction)
        counter += 1
    if counter % 2 == 0:
        if transaction < 10:
            print("Error in transaction!")
        else:
            counter_card += 1
            money_card += transaction
            print("Product sold!")
    else:
        if transaction > 100:
            print("Error in transaction!")
        else:
            counter_cash += 1
            money_cash += transaction
            print("Product sold!")
    if money_cash + money_card >= expected_sum:
        sum_gathered = True
        break
    transaction = input()
if money_cash and counter_cash > 0:
    average_cash = money_cash / counter_cash
if money_card and counter_card > 0:
    average_card = money_card / counter_card
if event_end:
    print("Failed to collect required money for charity.")
if sum_gathered:
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")