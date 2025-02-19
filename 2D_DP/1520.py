# import sys
# sys.setrecursionlimit(40000)

# A, B = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(A)]

# def recursion(y, x):
#     global count
    
#     if y == A-1 and x == B-1:
#         count +=1
#     for add_y, add_x in [[-1,0], [1,0], [0,-1], [0,1]]:
#         mv_y, mv_x = y + add_y, x + add_x
#         if 0<= mv_y < A and 0<= mv_x < B:
#             if graph[y][x] > graph[mv_y][mv_x]:
#                 count = max(count, recursion(mv_y, mv_x))
                
        
#     return count 

# count = 0
# print(recursion(0,0))

#위 코드는 시간초과

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

A, B = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(A)]
dp = [[-1 for _ in range(B)] for _ in range(A)]

def recursion(y, x):
    
    
    if y == A-1 and x == B-1: #이걸 +=에서 =로만 바꿈,, 마지막 인덱스라면 1
        dp[y][x] = 1
        return dp[y][x]
    
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    for add_y, add_x in [[-1,0], [1,0], [0,-1], [0,1]]:
        mv_y, mv_x = y + add_y, x + add_x
        if 0 <= mv_y < A and 0 <= mv_x < B: #이동한 좌표가 범위를 벗어나지 않도록
            if graph[y][x] > graph[mv_y][mv_x]: #이동한 좌표가 전 좌표보다 작아야 함
                dp[y][x] += recursion(mv_y, mv_x)#이건 틀릴리가 없는데
                  
    return dp[y][x]


print(recursion(0,0))
print(dp)



