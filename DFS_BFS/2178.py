# from collections import deque

# N, M = map(int, input().split())
# graph = [list(map(int, input().rstrip())) for _ in range(N)]
# visited = [[0 for _ in range(M)] for _ in range(N)]
# dist = [[0 for _ in range(M)] for _ in range(N)]

# q = deque()
# q.append([0,0])
# visited[0][0] = 1
# dist[0][0] = 1

# while q:
#     _y, _x =  q.popleft()
    
#     for mv_y, mv_x in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
#         dy, dx = _y + mv_y, _x + mv_x
#         if 0 <= dy < N and 0 <= dx < M:
#             if graph[dy][dx] == 1 and visited[dy][dx] == 0:
#                 visited[dy][dx] = 1
#                 dist[dy][dx] = dist[_y][_x] + 1
#                 q.append([dy,dx])

# print(dist[N-1][M-1])

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
dist = [[1e9 for _ in range(M)] for _ in range(N)]

def recursion(y, x):
        
    for mv_y, mv_x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dy, dx = mv_y + y, mv_x + x
        if 0<= dy < N and 0<= dx < M:
            if graph[dy][dx] == 1:
                if dist[dy][dx] > dist[y][x] + 1:
                    dist[dy][dx] = dist[y][x] + 1
                    recursion(dy, dx)
              
dist[0][0] = 1  
recursion(0, 0)
print(dist[N-1][M-1])