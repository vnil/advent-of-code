import collections

nr_players = 416
marbles = 7197500
circle = collections.deque([0])

current = 0
currentPlayer = 0

players = {a: 0 for a in range(nr_players)}


for i in range(1, marbles):
    insert_pos = (current + 2) % len(circle)
    if i % 23 == 0:
        del_pos = (current - 7 + len(circle)) % len(circle)
        players[currentPlayer] += i + circle[del_pos]
        del circle[del_pos]
        current = del_pos
        currentPlayer = (currentPlayer + 1) % nr_players
        continue
    if insert_pos == 0:
        insert_pos = len(circle)
    circle.insert(insert_pos, i)
    current = insert_pos
    currentPlayer = (currentPlayer + 1) % nr_players

print(max(players.values()))
