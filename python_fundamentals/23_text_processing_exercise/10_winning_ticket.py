def ticket_symbols(ticket_given):
    count = 0
    symbol = ""
    for char in ticket_given:
        if char != symbol:
            if count >= 6:
                break
            count = 1
            symbol = char
        else:
            count += 1
    if symbol in "@#$^":
        return symbol * count
    else:
        return []


def no_match(half_1, half_2):
    return len(half_1) < 6 or len(half_2) < 6 or half_1[0] != half_2[0]


tickets = [x.strip() for x in input().split(",")]
for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    if ticket[0] * 20 == ticket and ticket[0] in "@#$^":
        print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
        continue
    ticket_half_1 = ticket_symbols(ticket[:10])
    ticket_half_2 = ticket_symbols(ticket[10:])
    if no_match(ticket_half_1, ticket_half_2):
        print(f'ticket "{ticket}" - no match')
        continue
    if len(ticket_half_1) < 10 or len(ticket_half_2) < 10:
        print(f'ticket "{ticket}" - {min(len(ticket_half_1), len(ticket_half_2))}{ticket_half_1[0]}')
        continue

