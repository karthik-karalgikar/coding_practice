def hurdleRace(k, height):
    # Write your code here
    if k > max(height):
        return 0
    else:   
        maxHeight = max(height)
        jumps = maxHeight - k
    
    return jumps

print(hurdleRace(1, [1, 2, 3, 3, 2]))

'''
TRACING - 

k = 1 (can jump 1 unit high as of now)
height = [1, 2, 3, 3, 2]

if k > max(height):
1 > 3 -> false

else:
    maxHeight = max(height)
    maxHeight = 3
    jumps = maxHeight - k
    jumps = 3 - 1
    jumps = 2

return jumps

Output = 2
'''