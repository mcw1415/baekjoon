import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    if A != B:
        graph[A].append([C, B])
        graph[B].append([C, A])

q = []
heapq.heappush(q, [0, 1])
answer = 0
while q:
    w, node = heapq.heappop(q)
    
    if visited[node] == 0:
        visited[node] = 1
        answer += w
        
        for _w, next in graph[node]:
            heapq.heappush(q, [_w, next])

print(answer)
    
    