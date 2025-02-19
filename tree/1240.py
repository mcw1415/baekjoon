from collections import deque

N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]
want = []
#부모가 없기에 양방향으로 설정해야 함
for _ in range(N-1):
    A, B, C = map(int, input().split())
    tree[A].append([C, B]) 
    tree[B].append([C, A])
    
for _ in range(M):
    want.append(list(map(int, input().split())))
    
for start, end in want:
    visited = [0 for _ in range(N+1)]
    dist = [0 for _ in range(N+1)]
    
    q = deque()
    q.append(start)
    visited[start] = 1
    
    while q:
        node = q.popleft()
        
        for weight, next in tree[node]:
            if visited[next] == 0:
                visited[next] = 1
                dist[next] = dist[node] + weight
                q.append(next)
    
    print(dist[end])
    
