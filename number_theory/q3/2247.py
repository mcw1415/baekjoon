# N = int(input())

# def SOD(n):
#     sum = 0
#     for i in range(2, n):
#         if n % i == 0:
#             sum += i
            
#     return sum

# def CSOD(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += SOD(i)
        
#     return sum

# print(CSOD(N))

# #위 코드는 시간초과
# N = int(input())

# temp = 0
# for i in range(2, N+1):
#     temp += (N//i) * i - i

# print(temp%1_000_000)

#
N = int(input())

temp = 0
for i in range(2, N//2 + 1):
    temp += (N//i) * i - i

print(temp%1_000_000)