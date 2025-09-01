from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end = " ")

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

graph = {
    'A' : ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bfs(graph, 'A')

'''
TRACING - 
visited = set([start]) -> set(['A'])
visited = {'A'}

queue = deque([start]) -> deque(['A'])

while queue:
    node = queue.popleft() (queue = ['A'])
    queue = []
    node = 'A'

    print(node, end = " ")
    Current output = A

    for i in graph[node]: -> 'A' : ['B', 'C']
        i = B
        if i not in visited:
        -> B not in visited
            visited.add(i)
            => visited = {'A', 'B'}
            queue.append(i)
            => queue = ['B']
        
        i = C
        if i not in visited:
        -> C not in visited
            visited.add(i)
            => visited = {'A', 'B', 'C'}
            queue.append(i)
            => queue = ['B', 'C']

    -------------------------------------------------------------
    node = queue.popleft() (queue = ['B', 'C'])
    queue = ['C']
    node = 'B'

    print(node, end = " ")
    Current Output = A B

    for i in graph[node]: -> 'B': ['A', 'D', 'E']
        i = A
        if i not in visited:
        -> A is in visited, does not go inside if statement

        i = D
        if i not in visited:
        -> D not in visited
            visited.add(i)
            => visited = {'A', 'B', 'C', 'D'}
            queue.append(i)
            => queue = ['C', 'D']

        i = E
        if i not in visited:
        -> E not in visited
            visited.add(i)
            => visited = {'A', 'B', 'C', 'D', 'E'}
            queue.append(i)
            => queue = ['C', 'D', 'E']
   
    -------------------------------------------------------------
    node = queue.popleft() (queue = ['C', 'D', 'E'])
    queue = ['D', 'E']
    node = 'C'

    print(node, end = " ")
    Current Output = A B C

    for i in graph[node]: -> 'C': ['A', 'F']
        i = A
        if i not in visited:
        -> A in visited, will not go inside if statement

        i = F
        if i not in visited:
        -> F not in visited:
            visited.add(i)
            => visited = {'A', 'B', 'C', 'D', 'E', 'F'}
            queue.append(i)
            => queue = ['D', 'E', 'F']

    -------------------------------------------------------------
    node = queue.popleft() (queue = ['D', 'E', 'F'])
    queue = ['E', 'F']
    node = 'D'

    print(node, end = " ")
    Current Output = A B C D

    for i in graph[node]: -> 'D': ['B']
        i = B
        if i not in visited:
        -> B in visited

    -------------------------------------------------------------
    node = queue.popleft() (queue = ['E', 'F'])
    queue = ['F']
    node = 'E'

    print(node, end = " ")
    Current Output = A B C D E

    for i in graph[node]: -> 'E': ['B', 'F'],
        i = B
        if i not in visited:
        -> B in visited

        i = F
        if i not in visited:
        -> F in visited

    -------------------------------------------------------------
    node = queue.popleft() (queue = ['F'])
    queue = []
    node = 'F'

    print(node, end = " ")
    Current Output = A B C D E F

    for i in graph[node]: -> 'F': ['C', 'E']
        i = C
        if i not in visited:
        -> C in visited

        i = E
        if i not in visited:
        -> E in visited
    
    -------------------------------------------------------------
    queue is empty, so come out of the while loop

Output = A B C D E F
    
        

'''
