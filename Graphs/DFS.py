def dfs(graph, node, visited):
    if node in visited:
        return 
    
    visited.add(node)
    print(node)
    for i in graph[node]:
        dfs(graph, i, visited)

visited = set()
graph = {
    'A' : ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
dfs(graph, 'A', visited)

'''
TRACING - 

node = 'A'
if node in visited:
-> A is not in visited

visited.add(node)
=> visited = {'A'}

print(node)
Current Output = A

for i in graph[node]:
    i = B
    dfs(graph, i, visited)
    dfs(graph, B, {'A'})

dfs(graph, B, {'A'}) -> 
node = 'B'
if node in visited:
-> B not in visited

visited.add(node)
=> visited = {'A', 'B'}

print(node)
Current Output = 
A
B

for i in graph[node]:
    i = A
    dfs(graph, A, {'A', 'B'})

dfs(graph, A, {'A', 'B'}) -> 
node = 'A'
if node in visited:
    returned   (A in visited)

for i graph[node]:
    i = D
    dfs(graph, D, {'A', 'B'})

dfs(graph, D, {'A', 'B'}) -> 
node = 'D'
if node in visited:
-> no

visited.add(node)
=> visited = {'A', 'B', 'D'}

print(node)
Current Output = 
A
B
D

for i in graph[node]: -> 'D' : ['B']
    i = B
    dfs(graph, B, {'A', 'B', 'D'})

dfs(graph, B, {'A', 'B', 'D'}) -> 
node = B
if node in visited:
-> yes, so return

for i in node[graph]: -> 'B': ['A', 'D', 'E'] (only a and d completed)
    i = E
    dfs(graph, E, {'A', 'B', 'D'})

dfs(graph, E, {'A', 'B', 'D'}) -> 
node = 'E'
if node in visited:
-> no

visited.add(node)
visited = {'A', 'B', 'D', 'E'}

print(node)
Current Output =
A
B
D
E

for i in node[graph]: -> 'E': ['B', 'F']
    i = B
    dfs(graph, B, {'A', 'B', 'D', 'E'})

dfs(graph, B, {'A', 'B', 'D', 'E'}) -> 
node = 'B'

if node in visited:
-> yes, so return

    i = F
    dfs(graph, F, {'A', 'B', 'D', 'E'})

dfs(graph, F, {'A', 'B', 'D', 'E'}) -> 
node = 'F'

if node in visited:
-> no

visited.add(node)
visited = {'A', 'B', 'D', 'E', 'F'}

print(node)
Current Output = 
A
B
D
E
F

for i in graph[node]: -> 'F': ['C', 'E']
    i = C
    dfs(graph, C, {'A', 'B', 'D', 'E', 'F'})

dfs(graph, C, {'A', 'B', 'D', 'E', 'F'}) -> 
node = 'C'

if node in visited:
-> no

visited.add(node)
visited = {'A', 'B', 'D', 'E', 'F', 'C'}

print(node)
Current Output = 
A
B
D
E
F
C

for i in node[graph]: -> 'C': ['A', 'F']
    i = A
    dfs(graph, A, visited)

dfs(graph, A, visited)
node = 'A'

if node in visited:
-> yes, so return

    i = F
    dfs(graph, F, visited)

dfs(graph, F, visited)
node = 'F'

if node in visited:
-> yes, so return

backtrack to F (line 137)

    i = 'E'
    dfs(graph, E, visited)

dfs(graph, E, visited)
node = 'E'

if node in visited:
-> yes, so return

all of them completed. 

Final Output = 
A
B
D
E
F
C

'''