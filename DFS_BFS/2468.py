#점화식 문제랑 그래프 유니온 파인드, 다익스트라 연습 많이 할 것
from collections import deque 

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_h = max(map(max, graph))+1
max_count = 0


for h in range(max_h):
    number = 1
    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            if graph[y][x] <= h or visited[y][x] != 0: #침수한 지역이거나 이미 방문했을 경우 패스
                continue
            q = deque()
            q.append([y,x])
            visited[y][x] = number
            
            while q:
                _y, _x = q.popleft()
            
                for mv_y, mv_x in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    dy, dx = _y + mv_y, _x + mv_x
                    if 0 <= dy < N and 0 <= dx < N and h < graph[dy][dx] and visited[dy][dx] == 0:
                        visited[dy][dx] = number
                        q.append([dy,dx])
                        
            number += 1
    max_count = max(max_count, number-1)        
            
        
print(max_count)

