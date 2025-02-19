# import heapq

# V, E = map(int, input().split())
# graph = [[] for _ in range(V+1)]
# visited = [0 for _ in range(V+1)]

# for _ in range(E):
#     A, B, C = map(int, input().split())
#     graph[A].append([C, B])
#     graph[B].append([C, A])

# q = []
# heapq.heappush(q, [0, 1])
# answer = 0

# while q:  
#     w, node = heapq.heappop(q)
    
#     if visited[node] != 0: #방문한 곳이라면 패스
#         continue
#     else: #아니라면 진행 
#         visited[node] = 1
#         answer += w
        
#         for _w, next in graph[node]:
#             if visited[next] == 0:
#                 heapq.heappush(q, [_w, next])
    
# print(answer)
def _find(A):
    if A == parent[A]:
        return A
    else:
        parent[A] = _find(parent[A])
        return parent[A]
    
def _union(A, B):
    a = _find(A)
    b = _find(B)
    
    if a == b:
        return 
    if Rank[a] > Rank[b]:
        parent[b] = a
    elif Rank[a] < Rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        Rank[a] += 1
    
V, E = map(int, input().split())
parent = [i for i in range(V+1)]
Rank = [0 for _ in range(V+1)]
links = []
for _ in range(E): #링크 싹 다 가져와
    links.append(list(map(int, input().split())))
links.sort(key= lambda x: x[2]) #순서대로 정렬

answer = 0
for A, B, C in links:
    if _find(A) != _find(B):
        _union(A, B)
        answer += C

print(answer)

#유니온 파인드 구현이 조금 더 쉬웠음


    