# A, B = map(int, input().split())
# power = [0 for _ in range(B-A+1)] #모든 수 각각의 지수를 담아놓을 리스트

# def recur(number, idx): 
#     if number % 2 == 0:
#         power[idx] += 1
#         recur(number//2, idx)
#         return
#     return 
# answer = 0

# for idx, i in enumerate(range(A, B+1)):
#     recur(i, idx)
#     answer += 2**power[idx]
# print(answer)
# 메모리 초과 위 코드는

A, B = map(int, input().split())
A -=1
tmp_A = A
for i in range(1, 99):
    tmp_A += (A//(2**i)) * ((2**i) - (2**(i-1)))
    
tmp_B = B
for i in range(1, 99):
    tmp_B += (B//(2**i)) * ((2**i) - (2**(i-1)))

print(tmp_B - tmp_A)