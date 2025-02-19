# N = int(input())

# dp = [0 for _ in range(N+1)]
# for idx in range(1, N+1):
#     if idx < 3:
#         dp[idx] = idx
#     else:   
#         dp[idx] = dp[idx-1] + dp[idx-2]
    
# print(dp[N]%10007)

N = int(input())
dp = [-1 for _ in range(N)]

def recursion(idx):
    if idx >= N+1:
        return 0 
    if idx == N:
        return 1
    if dp[idx] != -1:
        return dp[idx]
    
    #1x2를 넣는 경우와 2X1를 넣는 경우
    dp[idx] = recursion(idx + 2) + recursion(idx + 1)
    
    return dp[idx]

recursion(0)
print(dp)
print(max(dp)%10_007)