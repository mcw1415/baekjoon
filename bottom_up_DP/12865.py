N, limit_weight = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

# def recursion(idx, weight):
#     if weight > limit_weight:
#         return -1e9
    
#     if idx == N:
#         return 0
    
#     if dp[idx][weight] != -1:
#         return dp[idx][weight]
    
#     #상품 선택하거나 안한 경우 
#     dp[idx][weight] = max(recursion(idx + 1, weight + items[idx][0]) + items[idx][1], recursion(idx + 1,weight))
    
#     return dp[idx][weight]
    
dp = [[0 for _ in range(100_001)] for _ in range(N+1)]

for idx in range(N)[::-1]: #뒤에서부터 인덱스를 돌아 
    for weight in range(limit_weight):
        if weight + items[idx][0] > limit_weight:
            dp[idx][weight] = dp[idx+1][weight]
        else:
            dp[idx][weight] = max(dp[idx + 1][weight + items[idx][0]] + items[idx][1], dp[idx + 1][weight])

print(max(dp[0]))

