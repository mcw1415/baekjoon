import sys
sys.setrecursionlimit(10000)

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(N)] for _ in range(N)]

def recursion(y, x):
    
    if y >= N or x >= N: #범위를 벗어났다면 경우가 없으니 0
        return 0
    
    if y == N-1 and x == N-1: #끝에 도달했다면(수정)
        return 1
    
    if map[y][x] == 0:
        return 0
    
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = recursion(y + map[y][x], x) + recursion(y, x + map[y][x])
    
    return dp[y][x]
    
print(recursion(0,0))


# 2 3 3 1
# 1 2 1 3
# 1 2 3 1
# 3 1 1 0