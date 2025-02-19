# import sys
# sys.setrecursionlimit(400000)

# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# answer = 0
# def recursion(y, x, count): # 카운트 3이 왔다 쳐 근데 아무것도 없을 경우 반환을 해야 하는데
#     global answer
    
#     for mv_y, mv_x in [[-1, 0], [1, 0], [0, -1], [0, 1]]: #상하좌우
#         dy, dx = y + mv_y, x + mv_x
#         if 0 <= dy < N and 0 <= dx < N:
#             if graph[dy][dx] > graph[y][x]: 
#                 recursion(dy, dx, count + 1)

#     answer = max(answer, count)
    

# for init_y in range(N):
#     for init_x in range(N):
#         recursion(init_y, init_x, 1)
        
# print(answer)

# import sys
# sys.setrecursionlimit(400000)

# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0 for _ in range(N)] for _ in range(N)]

# def recursion(y, x): 
#     if dp[y][x] != 0:
#         return dp[y][x]
    
#     for mv_y, mv_x in [[-1, 0], [1, 0], [0, -1], [0, 1]]: #상하좌우
#         dy, dx = y + mv_y, x + mv_x
#         if 0 <= dy < N and 0 <= dx < N: #범위를 벗어나면 x
#             if graph[dy][dx] > graph[y][x]: #이전보다 커야겠지
#                 dp[y][x] = max(dp[y][x], recursion(dy, dx) + 1) 
    
#     return dp[y][x]

# for init_y in range(N):
#     for init_x in range(N):
#         recursion(init_y, init_x)
        
# print(max(map(max, dp))+1)

import sys
sys.setrecursionlimit(400000)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
#점화식을 바탕으로 전개하기 위해
for_BUDP = [[graph[y][x], y, x] for x in range(N) for y in range(N)]
for_BUDP.sort(key= lambda x: x[0])

for daenamoo_cost, y, x in for_BUDP:
        for mv_y, mv_x in [[-1, 0], [1, 0], [0, -1], [0, 1]]: #상하좌우
            dy, dx = y + mv_y, x + mv_x
            if 0 <= dy < N and 0 <= dx < N: #범위를 벗어나면 x
                if graph[dy][dx] > graph[y][x]: #이전보다 커야겠지
                    dp[dy][dx] = max(dp[y][x] + 1, dp[dy][dx])


print(dp)
        
        
# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0] * N for _ in range(N)]

# # 모든 좌표와 대나무 양을 함께 저장한 후, 대나무 양 기준으로 정렬
# cells = [(graph[y][x], y, x) for y in range(N) for x in range(N)]
# cells.sort()  # 대나무 양 오름차순 정렬

# # 상하좌우 이동 방향
# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# # Bottom-Up 방식으로 DP 채우기
# for bamboo, y, x in cells:
#     for mv_y, mv_x in directions:
#         dy, dx = y + mv_y, x + mv_x
#         if 0 <= dy < N and 0 <= dx < N and graph[dy][dx] > graph[y][x]:
#             dp[dy][dx] = max(dp[dy][dx], dp[y][x] + 1)

# # 최대 방문 칸 수 출력
# print(max(map(max, dp)) + 1)
