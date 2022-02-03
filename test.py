field =[int(cell) for row in range(0,3) for cell in input().split()]

winner = 0
for player_num in range(1, 3):
    player_cells = [cell == player_num for cell in field]
    win = all(player_cells[0:3]) or all(player_cells[3:6]) or all(player_cells[6:9]) or \
          all(player_cells[0::3]) or all(player_cells[1::3]) or all(player_cells[2::3]) or \
          all(player_cells[0::4]) or all(player_cells[2:6:2])
    if win:
        winner = player_num
        break

if winner == 0:
    print("Draw!")
elif winner == 1:
    print("First player won")
else:
    print("Second player won")