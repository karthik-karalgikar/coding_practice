def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = list(set(ranked))
    ranked.sort()
    n = len(ranked)
    i = 0
    result = []
    
    for score in player:
        while i < n and ranked[i] <= score:
            i = i + 1
        result.append(n - i + 1)
        
    return result

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
