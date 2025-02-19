N = int(input())
counsel_list = [list(map(int, input().split())) for _ in range(N)]

def recursion (idx):
    if idx > N:
        return -1e9
    if idx == N:
        return 0 
    if dp[idx] != -1:
        return dp[idx]
    #상담을 받거나, 안받거나
    dp[idx] = max(recursion(idx + counsel_list[idx][0]) + counsel_list[idx][1], recursion(idx+1))
    
    return dp[idx]
    
    
dp = [-1 for _ in range(N)]

recursion(0)
print(dp)
print(max(dp))