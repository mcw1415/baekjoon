# N, K = map(int, input().split())
# arr = []
# for _ in range(N):
#     a = int(input())
#     arr.append(a)    

# #가치가 같은 동전 여러개가 주어질 수도 있음
# #각 각의 동전은 여러 번 사용해도 됨
# #그래서 결국 K 가치로 맞춰야 함

# #백트래킹으로 풀 것이냐 점화식으로 풀 것이냐

# def recursion(idx, value, count): 
#     global min_count
    
#     if value > K: #원하는 가치보다 더 높을 경우
#         return 
    
#     if value == K: #원하는 가치랑 같을 경우
#         min_count = min(count, min_count)
#         return 
    
#     if idx == N: #인덱스 초과할 경우
#         return
    
#     #한번 더 사용하는 경우
#     recursion(idx, value + arr[idx], count + 1)
#     #아님 넘어가는 경우
#     recursion(idx+1, value, count)

# min_count = 1e9
# recursion(0,0,0)
# print(min_count)

#다시 풀어볼 것 맞긴 함
import sys
sys.setrecursionlimit(40000)
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
   
dp = [1e9 for _ in range(K+1)] #왜 가치로 하는거지

def recursion(value): 
    
    if value > K: #원하는 가치를 초과할 경우이거나 인덱스 초과했을 때
        return 1e8
    
    if value == K: #원하는 가치일 경우 더이상 동전이 필요하지 않으니까
        return 0

    if dp[value] != 1e9:
        return dp[value]
    
    #한번 더 사용하는 경우와 넘어가는 경우 둘 중의 최소 값을 넣어야 함.
    for _value in arr:
        dp[value] = min(dp[value], recursion(value + _value) + 1)
    
    return dp[value]

answer = recursion(0)
if answer >= 1e8:
    print(-1)
else:
    print(answer)
