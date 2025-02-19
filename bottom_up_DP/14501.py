N = int(input())
counsel_list = [list(map(int, input().split())) for _ in range(N)]

# def recursion (idx):
#     if idx > N:
#         return -1e9
#     if idx == N:
#         return 0 
#     if dp[idx] != -1:
#         return dp[idx]
#     #상담을 받거나, 안받거나
#     dp[idx] = max(recursion(idx + counsel_list[idx][0]) + counsel_list[idx][1], recursion(idx+1))
    
#     return dp[idx]
    
    
dp = [0 for _ in range(N+1)]

for idx in range(N)[::-1]:
    if idx + counsel_list[idx][0] > N-1:
        dp[idx] = dp[idx+1]
    else:
        dp[idx] = max(dp[idx + counsel_list[idx][0]] + counsel_list[idx][1], dp[idx+1])
        # dp[6] = max(dp[6+2]+200, dp[7]) if문 걸리는 것들
        # dp[5] = max(dp[5+4]+50, dp[6]) if문 걸려서 것들
        # dp[4] = max(dp[4+2]+15, dp[5]) 15
        # dp[3] = max(dp[3+4]+20, dp[4]) 35
        # dp[2] = max(dp[2+1]+10, dp[3]) 45
        # dp[1] = max(dp[1+5]+20, dp[2]) 45
        # dp[0] = max(dp[0+3]+10, dp[1]) 45 
print(dp)