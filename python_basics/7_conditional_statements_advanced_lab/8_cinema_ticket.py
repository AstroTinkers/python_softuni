day = input()
ticket_price = 0
if day in 'Monday Tuesday Friday':
    ticket_price = 12
elif day in 'Wednesday Thursday':
    ticket_price = 14
elif day in 'Saturday Sunday':
    ticket_price = 16
print(ticket_price)