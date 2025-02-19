# N = int(input())
# N_arr = sorted(list(map(int, input().split())))

# M = int(input())
# M_arr = list(map(int, input().split()))
# answer = [0 for _ in range(M)]

# for idx, num in enumerate(M_arr):
#     s_p = 0
#     e_p = N-1
    
#     Flag = 0
#     while s_p <= e_p:
        
#         mid_p = (s_p + e_p)//2
        
#         if N_arr[mid_p] == num: 
#             Flag = 1
#             break

#         if N_arr[mid_p] < num:
#             s_p = mid_p + 1
#             continue
            
#         if N_arr[mid_p] > num:
#             e_p = mid_p - 1
#             continue
        
#     answer[idx] = Flag
    
# print(*answer)

#M이 정렬된다고 하면 answer를 구할 방법이 없음

N = int(input())
N_arr = list(map(int, input().split()))

M = int(input())
M_arr = list(map(int, input().split()))
answer = [0 for _ in range(M)]

for idx, M_num in enumerate(M_arr):
    for N_num in N_arr:
        if M_num == N_num:
            answer[idx] = 1
    
print(*answer)