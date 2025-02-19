#bottomup

STR1 = list(input())
STR2 = list(input())
N1 = len(STR1)
N2 = len(STR2)
dp = [[0 for _ in range(N2+1)] for _ in range(N1+1)]

for y in range(N1):
    for x in range(N2):
        if STR2[x] == STR1[y]:
            dp[y+1][x+1] = dp[y][x] + 1
        else:
            dp[y+1][x+1] = max(dp[y+1][x], dp[y][x+1])
            
print(max(map(max,dp)))