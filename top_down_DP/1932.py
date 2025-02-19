# N = int(input())
# t = [list(map(int, input().split())) for _ in range(N)]

# def recursion(idx, value, direction):
#     global maximum
    
#     if idx == N:
#         maximum = max(maximum, value)
#         return
    
#     #왼쪽
#     recursion(idx + 1, value + t[idx][direction], direction)
    
#     #오른쪽
#     recursion(idx + 1, value + t[idx][direction], direction + 1)   
    
# maximum = 0
# recursion(0,0,0)
# print(maximum)

N = int(input())
t = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

def recursion(idx, direction):
    
    if idx == N: #더이상 내려갈 곳이 없으니까 0 반환
        return 0
    
    if dp[idx][direction] != 0:
        return dp[idx][direction]
    
    #왼쪽 혹은 오른쪽
    dp[idx][direction] = max(recursion(idx + 1, direction) + t[idx][direction], recursion(idx + 1, direction + 1)+ t[idx][direction])   
    
    return dp[idx][direction]
    
answer = recursion(0,0)
print(answer)

#     7
#    3 8
#   8 1 0
#  2 7 4 4
# 4 5 2 6 5