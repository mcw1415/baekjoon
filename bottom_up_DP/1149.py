N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(3)] for _ in range(N+1)]

for idx in range(N):
    for rgb in range(3):
        if rgb == 0: #RED
            dp[idx+1][rgb] = min(dp[idx][1], dp[idx][2]) + RGB[idx][rgb]
        if rgb == 1: #GREEN
            dp[idx+1][rgb] = min(dp[idx][0], dp[idx][2]) + RGB[idx][rgb]
        if rgb == 2: #BLUE
            dp[idx+1][rgb] = min(dp[idx][0], dp[idx][1]) + RGB[idx][rgb]

print(min(dp[N]))

# arr = [[1, 2, 3], [4,5,6], [7,8,9], [10,11,12]]
# print(len(arr))

#탑다운으로 가봅시다잉 우선 재귀~
# N = int(input())
# RGB = [list(map(int, input().split())) for _ in range(N)]
# min_value = 1e9

# def recursion(idx, color, value):
#     global min_value
        
#     if idx == N:
#         min_value = min(min_value, value)
#         return
          
#     if color == 0: #전 컬러가 RED(0)이라면
#         recursion(idx+1, 1, value + RGB[idx][1])
#         recursion(idx+1, 2, value + RGB[idx][2])
#     elif color == 1: #전 컬러가 GREEN(1)이라면
#         recursion(idx+1, 0, value + RGB[idx][0])
#         recursion(idx+1, 2, value + RGB[idx][2])
#     else: #전 컬러가 BLUE(2)이라면
#         recursion(idx+1, 0, value + RGB[idx][0])
#         recursion(idx+1, 1, value + RGB[idx][1])
    
# recursion(0, 0, 0)
# recursion(0, 1, 0)
# recursion(0, 2, 0)

# print(min_value)
        
#탑다운
# import sys
# sys.setrecursionlimit(40000)

# N = int(input())
# RGB = [list(map(int, input().split())) for _ in range(N)]
# dp = [[-1 for _ in range(3)] for _ in range(N)]

# def recursion(idx, rgb):
        
#     if idx == N:
#         return 0
#     if dp[idx][rgb] != -1:
#         return dp[idx][rgb]
    
#     if rgb == 0:
#         dp[idx][rgb] = min(recursion(idx+1, 1) + RGB[idx][1], recursion(idx+1, 2) + RGB[idx][2])
#     if rgb == 1:
#         dp[idx][rgb] = min(recursion(idx+1, 0) + RGB[idx][0], recursion(idx+1, 2) + RGB[idx][2])
#     if rgb == 2:
#         dp[idx][rgb] = min(recursion(idx+1, 0) + RGB[idx][0], recursion(idx+1, 1) + RGB[idx][1])
    
#     return dp[idx][rgb]

# for i in range(3):
#     recursion(0,i)

# print(min(dp[0]))


        