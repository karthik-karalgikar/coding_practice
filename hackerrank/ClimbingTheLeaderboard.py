def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = set(ranked)
    ranked = list(ranked)
    positions = []
    for i in range(len(player)):
        ranked.append(player[i])
        
    ranked.sort(reverse=True)
    
    for i in range(len(ranked)):
        for j in range(len(player)):
            if player[j] == ranked[i]:
                positions.append(i + 1)
                
    return positions

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
