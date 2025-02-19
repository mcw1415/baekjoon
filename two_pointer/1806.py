N, S = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(N+1)]

for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]

s_p = 0
e_p = 1
answer = 1e9
while e_p <= N:
    
    if prefix[e_p] - prefix[s_p] < S:
        e_p += 1
        continue
        
    if prefix[e_p] - prefix[s_p] >= S:
        answer = min(answer, e_p - s_p)
        s_p += 1
        continue

if answer == 1e9:
    print(0)
else:
    print(answer)
        
#arr :    5  1  3   5  10   7   4   9   2   8
#prefix : 0  5, 6, 9, 14, 24, 31, 35, 44, 46, 54
#15이상인 것만 찾으면 되는거 아냐?
