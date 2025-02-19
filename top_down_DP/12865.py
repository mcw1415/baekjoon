# N, limit_weight = map(int, input().split())
# items = [list(map(int, input().split())) for _ in range(N)]

# def recursion(idx, weight):
#     if weight > limit_weight:
#         return -1e9
    
#     if idx == N:
#         return 0
    
#     if dp[idx][weight] != -1:
#         return dp[idx][weight]
    
#     #상품 선택하거나 안한 경우 
#     dp[idx][weight] = max(recursion(idx + 1, weight + items[idx][0]) + items[idx][1], recursion(idx + 1, weight))
    
#     return dp[idx][weight]
    
# dp = [[-1 for _ in range(100_001)] for _ in range(N)]

# ans = recursion(0,0)
# print(ans)


N, limit_weight = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

def recursion(idx, weight):
    if weight > limit_weight:
        return -1e9
    
    if idx == N:
        return 0
    
    if dp[idx] != -1:
        return dp[idx]
    
    #상품 선택하거나 안한 경우 
    dp[idx] += max(recursion(idx + 1, weight + items[idx][0]) + items[idx][1], recursion(idx + 1, weight))
    print(dp[idx])
    return dp[idx]
    
dp = [-1  for _ in range(N)]

ans = recursion(0,0)
print(dp)
print(ans)

