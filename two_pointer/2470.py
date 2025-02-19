# N = int(input())
# arr = sorted(list(map(int, input().split())))


# s_p = 0
# e_p = N-1
# min_diff = 1e9
# answer = []
# while s_p < e_p:
#     sum = arr[s_p] + arr[e_p] # 두 수의 합
#     diff = abs(0-sum) #0과의 차이  
    
#     #차이가 더 작아졌다면
#     if diff <= min_diff: 
#         min_diff = diff
#         answer.append([arr[s_p], arr[e_p]])
#         s_p += 1
        
    
#     #차이가 더 크거나 같아졌다면 
#     if diff > min_diff:
#         e_p += 1

# print(*answer[-1])
    
N = int(input())
arr = sorted(list(map(int, input().split())))

s_p = 0
e_p = N-1
min_diff = 1e10
answer = []

while s_p < e_p:
    sum = arr[s_p] + arr[e_p] # 두 수의 합
    diff = abs(0-sum) #0과의 차이 
    
    if diff < min_diff:
        min_diff = diff
        answer.append([arr[s_p], arr[e_p]])
    
    #합이 0이라면 
    if sum == 0:
        break
    
    #합이 음의 정수라면 
    if sum < 0: 
        s_p += 1
        
    #합이 양의 정수라면
    if sum > 0:
        e_p -= 1

print(answer)
print(*answer[-1])


# 5
# -2 4 -99 -1 98
# -> -99 -2 -1 4 98
# -> 0 -99 -101 -102 -98 0
# -2 2 -99 -1 98
# -> -99 -2 -1 2 98

#다 산성이거나 알칼리성인 경우
# 1 1 1 1 1 -> 1 1
# 1 2 3 4 5 -> 1 2

#인덱스 에러일 경우 최댓값 기준을 잘 보자