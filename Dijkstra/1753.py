import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
dist = [1e9 for _ in range(V+1)]
links = [[] for _ in range(V+1)]

for i in range(E):
    x, y, w = map(int, input().split())
    links[x].append([y, w])


q = []
heapq.heappush(q, [0, start])
dist[start] = 0

while q:
    _weight, node = heapq.heappop(q)
    
    for next, weight in links[node]:
        if dist[next] > dist[node] + weight:
            dist[next] = dist[node] + weight
            heapq.heappush(q, [dist[next], next])

for i in range(1, V+1):
    if dist[i] == 1e9:
        print('INF')
    else:
        print(dist[i])
    
        
        
