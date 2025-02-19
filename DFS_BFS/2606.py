# import sys
# sys.setrecursionlimit(10000)

# V = int(input())
# E = int(input())

# graph = [[] for _ in range(V+1)]
# visited = [0 for _ in range(V+1)]

# for _ in range(E):
#     A, B = map(int, input().split())
#     graph[A].append(B)
#     graph[B].append(A)

# def recursion(node):
#     global answer
    
#     for next in graph[node]:
#         if visited[next] == 0:
#             visited[next] = 1
#             answer += 1
#             recursion(next)
                     
# answer = 0
# visited[1] = 1
# recursion(1)
# print(answer)

from collections import deque
            
V = int(input())
E = int(input())

graph = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    
q = deque()
q.append(1)
visited[1] = 1
count = 0

while q:
    node = q.popleft()
    
    for next in graph[node]:
        if visited[next] == 0:
            visited[next] = 1
            q.append(next)
            count += 1

print(count)



