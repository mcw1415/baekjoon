# N = int(input())
# arr = [int(input()) for _ in range(N)]

# def recursion(idx, v, con):
#     global max_v
#     if con == 3:
#         return 
    
#     if idx == N:
#         max_v = max(max_v, v)
#         return
    
#     #마시는 경우
#     recursion(idx + 1, v + arr[idx], con + 1)
    
#     #넘기는 경우
#     recursion(idx + 1, v, 0)

# max_v = 0
# recursion(0, 0, 0)
# print(max_v)

import sys
sys.setrecursionlimit(100000)

N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [[-1 for _ in range(3)] for _ in range(N)]

def recursion(idx, con):
    if con == 3:
        return -1e9
    
    if idx == N:
        return 0
    
    if dp[idx][con] != -1:
        return dp[idx][con]
    
    #마시는 루트, 안마신 루트 중에서 높은 값
    dp[idx][con] = max(recursion(idx + 1, con + 1) + arr[idx], recursion(idx + 1, 0))
    
    return dp[idx][con]

print(recursion(0, 0))