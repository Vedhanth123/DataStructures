

# 1) rank the number of players in leaderboard array
# 2) compare alice scores with the leaderboard array

ranked_list = [100, 100, 50, 40, 40, 20, 10]
ranked_list = list(set(ranked_list))

ranked_list.sort(reverse=True)
player_score = [5 ,25 ,50, 120]

rank = 1

x = 0
while(player_score[0] < ranked_list[x] or x > len(ranked_list)):
    x += 1

print(rank)
print(ranked_list)

