#완전탐색
#누적합
#투포인터

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# #arr 정리 -> 이것도 max_height_x에서 기둥이 가장 높은게 두개라면 리스트로 반환될거임
# arr.sort(key=lambda x: x[0])
# max_height = max(arr, key=lambda x: x[1])[1]
# max_height_x = max(arr, key=lambda x: x[1])[0]
# first_x = min(arr, key=lambda x: x[0])[0]
# last_x = max(arr, key=lambda x: x[0])[0]

# x_arr = [x[0] for x in arr]

# update_value_l,lower_sum = 0, 0
# for l in range(first_x, max_height_x): #x축 돌기
#     if l in x_arr: #x값이 주어진 x_arr에 있냐
#         index = x_arr.index(l)
#         if arr[index][1] > update_value_l: #있으면 update value보다 크냐
#             lower_sum += arr[index][1] #크면 lower_sum에 넣어
#             update_value_l = arr[index][1] #업데이트도 해주고
#         else:
#             lower_sum += update_value_l
            
#     else:
#         lower_sum += update_value_l #x_arr에 없으면 update_value_l값을 걍 써
# print(lower_sum)
   
# update_value_u, upper_sum = 0, 0
# for u in range(last_x, max_height_x, -1): 
#     if u in x_arr: #x값이 주어진 x_arr에 있냐
#         index = x_arr.index(u)
#         if arr[index][1] > update_value_u: #있으면 update value보다 크냐
#             upper_sum += arr[index][1] #크면 upper_sum에 넣어
#             update_value_u = arr[index][1] #업데이트도 해주고
#         else:
#             upper_sum += update_value_u
#     else:
#         upper_sum += update_value_u #x_arr에 없으면 update_value_u값을 걍 써
# print(upper_sum)
    
# answer = lower_sum + upper_sum + max_height
# print(answer)
# 이 코드의 문제점은 가운데에 가장 높은 기둥이 두개이고 띄워져 있다면? 어칼래

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

#arr 정리 -> 이것도 max_height_x에서 기둥이 가장 높은게 두개라면 리스트로 반환될거임
arr.sort(key=lambda x: x[0])
max_height = max(x[1] for x in arr)
max_height_x = [x[0] for x in arr if x[1] == max_height]
first_x = min(arr, key=lambda x: x[0])[0]
last_x = max(arr, key=lambda x: x[0])[0]

x_arr = [x[0] for x in arr]

update_value_l,lower_sum = 0, 0
for l in range(first_x, max_height_x[0]): #x축 돌기
    if l in x_arr: #x값이 주어진 x_arr에 있냐
        index = x_arr.index(l)
        if arr[index][1] > update_value_l: #있으면 update value보다 크냐
            lower_sum += arr[index][1] #크면 lower_sum에 넣어
            update_value_l = arr[index][1] #업데이트도 해주고
        else:
            lower_sum += update_value_l
            
    else:
        lower_sum += update_value_l #x_arr에 없으면 update_value_l값을 걍 써
print(lower_sum)
   
update_value_u, upper_sum = 0, 0
for u in range(last_x, max_height_x[-1], -1): 
    if u in x_arr: #x값이 주어진 x_arr에 있냐
        index = x_arr.index(u)
        if arr[index][1] > update_value_u: #있으면 update value보다 크냐
            upper_sum += arr[index][1] #크면 upper_sum에 넣어
            update_value_u = arr[index][1] #업데이트도 해주고
        else:
            upper_sum += update_value_u
    else:
        upper_sum += update_value_u #x_arr에 없으면 update_value_u값을 걍 써
print(upper_sum)
    
answer = lower_sum + upper_sum + max_height*(max_height_x[-1] - max_height_x[0] + 1)
print(answer)