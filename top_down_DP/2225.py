import sys
sys.setrecursionlimit(4000)

N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

def recursion(value, count):
    
    if count > K or value > N:
        return 0
    
    if count == K and value == N:
        return 1
    
    if dp[value][count] != 0:
        return dp[value][count]

        
    for i in range(N+1):
        dp[value][count] += recursion(value + i, count + 1)
    
    return dp[value][count]

print(recursion(0,0)%1_000_000_000)



#중복조합의 경우 반복문으로 돌 것 
#1113
#1104
#바텀업으로 풀 것
