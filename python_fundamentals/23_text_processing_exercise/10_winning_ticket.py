import re


def ticket_symbols(ticket_given):
    list_temp = re.findall("(@)(#)($)(^)+", "".join(ticket_given))
    if len(list_temp) == 0:
        return list_temp
    count = {}
    for char in list_temp:
        count.setdefault(char, 0)
        if char in count:
            count[char] += 1
    max_count = max(count, key=count.get)
    return [el for el in (max_count * count[max_count])]


def no_match(half_1, half_2):
    return len(half_1) < 6 or len(half_2) < 6 or half_1[0] != half_2[0]


tickets = [x.strip() for x in input().split(",")]
for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    ticket_half_1 = ticket_symbols(ticket[:10])
    ticket_half_2 = ticket_symbols(ticket[10:])
    if no_match(ticket_half_1, ticket_half_2):
        print(f'ticket "{ticket}" - no match')
        continue
    if len(ticket_half_1) < 10 or len(ticket_half_2) < 10:
        print(f'ticket "{ticket}" - {min(len(ticket_half_1), len(ticket_half_2))}{ticket_half_1[0]}')
        continue
    print(f'ticket "{ticket}" - 10{ticket_half_1[0]} Jackpot!')
