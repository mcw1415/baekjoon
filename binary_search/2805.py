# N, M = map(int, input().split())
# t_arr = list(map(int, input().split()))

# s_p = 0
# e_p = max(t_arr)

# #원하는 무게를 맞출 때까지

# while s_p <= e_p:
#     sum = 0
#     for t in t_arr:
#         if t > s_p:
#             sum += t - s_p
        
#     if sum == M:
#         print(s_p)
#         break
    
#     s_p += 1
    
# N, M = map(int, input().split())
# t_arr = list(map(int, input().split()))

# s_h = 0
# e_h = max(t_arr)
# answer = []

# #원하는 무게를 맞출 때까지
# while s_h <= e_h:
#     mid_h = (s_h + e_h)//2 
    
#     sum = 0
#     for t in t_arr:
#         if t > mid_h:
#             sum += t - mid_h
    
    
#     if sum >= M: #벌목한 양이 요구하는 양보다 적으면 높이 내리기
#         if sum == M:
#             answer.append([sum, mid_h])
#             break
#         else:
#             answer.append([sum, mid_h])
#             s_h = mid_h + 1
#     if sum < M: #요구량보다 많으면 위로 올리기
#         e_h = mid_h - 1

# print(min(answer , key= lambda x: x[0])[1])
    
# 5 2000000000
# 900000000 900000000 900000000 900000000 900000000

N, M = map(int, input().split())
tree = list(map(int, input().split()))
answer = []

s_h = 0
e_h = max(tree)

while s_h <= e_h:
    
    m_h = (s_h + e_h) // 2
    
    sum = 0
    for t in tree:
        if t > m_h:
            sum += t - m_h
    
    if sum == M:
        answer.append([sum, m_h])
        break
    
    if sum > M: #벌목한 양이 초과했으면 절단기를 올려야겠지
        s_h = m_h + 1
        answer.append([sum, m_h])
        continue
        
    if sum < M: #벌목한 양이 부족했으면 절단기를 내려야겠지
        e_h = m_h - 1
        continue


print(min(answer, key= lambda x : x[0])[1])