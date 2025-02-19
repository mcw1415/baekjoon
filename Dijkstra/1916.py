import heapq
import sys
input = sys.stdin.readline

N = int(input())
Buses = int(input())
links = [[] for _ in range(N+1)]
dist = [1e9 for _ in range(N+1)]
for i in range(Buses):
    A, B, C = map(int, input().split())
    links[A].append([B, C])

start, dest = map(int, input().split())
    
q = []
heapq.heappush(q, [0, start])
dist[start] = 0

while q:
    _cost, node = heapq.heappop(q)
    
    if dist[node] >= _cost: 
        for next, cost in links[node]:
            if dist[next] > dist[node] + cost:
                dist[next] = dist[node] + cost
                heapq.heappush(q, [dist[next], next])
        
print(dist[dest])

##22번 라인에서 만약 (E,3), (E,2), (E,1)로 들어오면 모두 힙큐에 들어가게 되는데, 걸러주기 위해 추가한 조건문 
## -> 현재 넘어온 노드의 비용이 이미 저장된 노드의 비용보다 작거나 같아야 함.ㅜ ㅗㅗ 