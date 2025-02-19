import heapq
#visited 없어도 됨 가중치 업데이트 하기 위해서는 다익스트라에서는 그렇다고
N, M = map(int, input().split()) #1부터 N까지의 가중치 최소
graph = [[] for _ in range(N+1)]
dist = [1e9 for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split()) #A, B는 헛간이고 C는 소의 마리수(가중치) -> 결국 가중치가 가장 작은 값으로 곳간을 돌아다녀서 가중치의 합을 구하라는 문제임
    graph[A].append([C, B])
    graph[B].append([C, A])

q = []
dist[1] = 0
heapq.heappush(q, [dist[1], 1])

while q:
    w, start = heapq.heappop(q)
    
    for _w, _next in graph[start]:
        if dist[_next] > w + _w:
            dist[_next] =  w + _w
            heapq.heappush(q, [dist[_next], _next])

print(dist[N])
        

