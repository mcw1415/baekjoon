import time

N = int(input())
arr = list(map(int, input().split()))
X = int(input())
start = time.time()
check = [0 for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(N):
        if i == j or check[i] == 1 or check[j] == 1: 
            continue
        if arr[i] + arr[j] == X:
            answer += 1
            check[i], check[j] = 1, 1 #쌍이 확정되면 1로 체크
            

print(answer)
end = time.time()
print(f"{end - start:.5f} sec")