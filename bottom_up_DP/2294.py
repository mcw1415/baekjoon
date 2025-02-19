N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
dp = [1e9 for _ in range(K+1)]
dp[0] = 0

for c in arr:
    for v in range(c, K+1):
        dp[v] = min(dp[v], dp[v-c] + 1) #v-c가치일 때 필요한 동전 개수 왜 1을 추가하는거지

if dp[K] == 1e9:
    print(-1)
else:
    print(dp[K])