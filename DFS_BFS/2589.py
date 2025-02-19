from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(N)]

answer = 0
for y in range(N):
    for x in range(M):
        if graph[y][x] != 'L': #시작점이 육지가 아니라면 넘어가기 
            continue
        visited = [[0 for _ in range(M)] for _ in range(N)]
        dist = [[0 for _ in range(M)] for _ in range(N)] #아래로 내림
        
        q = deque()
        q.append([y,x])
        visited[y][x] = 1
        
        while q:
            _y, _x = q.popleft()
                
            for mv_y, mv_x in [[0, -1],[0, 1], [-1, 0],[1, 0]]: #어느 방향으로 움직일건데?
                dy = _y + mv_y
                dx = _x + mv_x
                
                if 0 <= dy < N and 0 <= dx < M: #움직인 방향이 범위를 벗어나지 않아야 함.
                    if graph[dy][dx] == 'L': #방문할 곳이 육지여야 함. 
                        if visited[dy][dx] == 0: #방문하지 않은 곳이어야 함
                            visited[dy][dx] = 1
                            dist[dy][dx] = dist[_y][_x] + 1
                            q.append([dy,dx]) 
        
        answer = max(answer, max(map(max, dist)))    
print(answer)

