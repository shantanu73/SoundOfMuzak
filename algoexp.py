def tournamentWinner(competitions, results):
    # Write your code here.
    points_table = {}

    i = 0

    while i < len(results):
        if results[i] == 1:
            winner = competitions[i][0]
        else:
            winner = competitions[i][1]

        print("\nWnner : "+ winner)

        if winner not in points_table.keys():
            points_table[winner] = 3
        else:
            points_table[winner] = points_table[winner] + 3
        print(points_table)
        i = i + 1

    win = ""
    win_pts = 0
    for keys, values in points_table.items():
        if values > win_pts:
            win_pts = values
            win = keys
    return win


comp = [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]]
results = [0, 1, 1]

print("\nWinner is:-\n")
print(tournamentWinner(comp, results))
