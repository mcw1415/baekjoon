# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# answer = [0 for _ in range(N+1)]

# for _ in range(M):
#     A, B = map(int, input().split()) #A가 B를 신뢰한다. 이 말은 B 먼저 해킹하면 A는 그냥 해킹할 수 있다. 따라서 B -> A 방향그래프임
#     graph[B].append(A)
    
# def recursion(node):
#     visited[node] = 1
    
#     for next in graph[node]:
#         if visited[next] == 0:
#             recursion(next)
    
# for start in range(1, N+1):
#     visited = [0 for _ in range(N+1)]
#     recursion(start)
#     answer[start] = visited.count(1)
    
# max_count = max(answer)
# for i in range(1, N+1):
#     if answer[i] == max_count:
#         print(i, end=' ')

#위 코드는 시간초과 -> 양갈래를 해결하지 못함
# import sys
# sys.setrecursionlimit(100000)

# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# answer = [-1 for _ in range(N+1)]

# for _ in range(M):
#     A, B = map(int, input().split()) #A가 B를 신뢰한다. 이 말은 B 먼저 해킹하면 A는 그냥 해킹할 수 있다. 따라서 B -> A 방향그래프임
#     graph[B].append(A)
    
# def recursion(node):
#     if answer[node] != -1:
#         return answer[node]
    
#     visited[node] = 1
#     count = 1
    
#     for next in graph[node]:
#         if visited[next] == 0:
#             count += recursion(next) 
    
#     answer[node] = count 
#     return count
    
# for start in range(1, N+1):
#     visited = [0 for _ in range(N+1)] #start할 때 이미 방문된 곳이라면 그냥 패스하자
#     recursion(start)

# max_count = max(answer)
# for i in range(1, N+1):
#     if answer[i] == max_count:
#         print(i, end=' ')
# print(answer)

# import sys
# sys.setrecursionlimit(100000)

# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# answer = [-1 for _ in range(N+1)]

# for _ in range(M):
#     A, B = map(int, input().split()) 
#     graph[B].append(A)
    
# def recursion(node):
#     count = 1
#     visited[node] = 1
    
#     for next in graph[node]: #4 -> 2, 3 -> 1 양갈래를 어떻게 해결할 것인데 d
#         if visited[next] == 0: 
#             count += recursion(next) 
    
#     answer[node] = count 
#     return count
    
# for start in range(1, N+1):
#     visited = [0 for _ in range(N+1)] 
#     recursion(start)

# max_count = max(answer)
# for i in range(1, N+1):
#     if answer[i] == max_count:
#         print(i, end=' ')
# print(answer)

#BFS
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
answer = [0 for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)
    
for start in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    q = deque()
    q.append(start)
    visited[start] = 1
    count = 1
    
    while q:
        node = q.popleft()
        
        for next in graph[node]:
            if visited[next] == 0:
                visited[next] = 1
                count += 1
                q.append(next)
    
    answer[start] = count 

max_count = max(answer)
for i in range(1, N+1):
    if max_count == answer[i]:
        print(i, end=' ')
    
    
    