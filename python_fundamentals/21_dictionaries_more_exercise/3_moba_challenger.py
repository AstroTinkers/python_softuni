def duel(p1, p2, player_data):
    if p1 in player_data and p2 in player_data:
        for pos in player_data[p1]:
            if pos in player_data[p2]:
                p1_total = sum(player_data[p1].values())
                p2_total = sum(player_data[p2].values())
                if p1_total > p2_total:
                    del player_data[p2]
                elif p2_total > p1_total:
                    del player_data[p1]
                break


def new_player(name, pos, skill_points, player_data):
    if name in player_data:
        if pos in player_data[name]:
            player_data[name][pos] = min(skill_points, player_data[name][pos])
        else:
            player_data[name][pos] = skill_points
    else:
        player_data[name] = {pos: skill_points}


def sorting_winners(player_data):
    for moba_player, moba_positions in player_data.items():
        player_data[moba_player] = {moba_position: moba_skill for moba_position, moba_skill in sorted(moba_positions.items(), key=lambda x: (-x[1], x[0]))}


def max_score(player_data):
    scores = {}
    for moba_pl, moba_poss in player_data.items():
        scores.setdefault(moba_pl, 0)
        for moba_pos, moba_points in moba_poss.items():
            scores[moba_pl] += moba_points
    scores = {moba_pl: moba_points for moba_pl, moba_points in sorted(scores.items(), key=lambda x: (-x[1], x[0]))}
    return scores


command = input()
players = {}
while not command == "Season end":
    if "vs" in command:
        player1, player2 = command.split(" vs ")
        duel(player1, player2, players)
    else:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        new_player(player, position, skill, players)
    command = input()
sorting_winners(players)
top_players = max_score(players)
for top_player in top_players.keys():
    print(f"{top_player}: {top_players[top_player]} skill")
    for role, skill in players[top_player].items():
        print(f"- {role} <::> {players[top_player][role]}")
