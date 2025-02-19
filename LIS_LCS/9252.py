STR1 = list(map(str,input().rstrip()))
STR2 = list(map(str,input().rstrip()))
dp = [[0 for _ in range(len(STR1)+1)] for _ in range(len(STR2)+1)]
answer = []

for y in range(len(STR2)):
    for x in range(len(STR1)):
        #비교할 문자가 같다면
        if STR2[y] == STR1[x]:
            dp[y+1][x+1] = dp[y][x] + 1

        #비교할 문자가 같지 않다면
        else:
            dp[y+1][x+1] = max(dp[y][x+1], dp[y+1][x])
            
print(max(map(max,dp)))
y, x = len(STR2), len(STR1)
while y > 0 and x > 0:
    if dp[y][x] == dp[y-1][x]:
        y -= 1
    elif dp[y][x] == dp[y][x-1]:
        x -= 1
    else:
        answer.append(STR1[x-1])
        x -= 1
        y -= 1

for s in answer[::-1]:
    print(s, end='')
