N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
dp = [0 for _ in range(K+1)]
dp[0] = 1 
for c in arr:
    for v in range(c, K+1):
        dp[v] += dp[v-c] #이 점화식이 납득이 잘 안됨

    print(dp)

#다시 풀어볼 것