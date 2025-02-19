N, M = map(int, input().split())
arr = list(map(int, input().split()))
interval = [list(map(int, input().split())) for _ in range(M)]

prefix = [0 for _ in range(N+1)]

for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]
    
for s, e in interval:
    print(prefix[e]- prefix[s-1])
    
    
# 5 3
# 5 4 3 2 1
# 1 3 -> 12
# 2 4 -> 9
# 5 5 -> 1