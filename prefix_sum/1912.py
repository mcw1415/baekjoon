N = int(input())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(N+1)]

for i in range(N):
    prefix[i+1] = max(prefix[i] + arr[i], arr[i])

max_value = -1e9
for i in range(1, N+1):
    max_value = max(prefix[i], max_value)

print(max_value)