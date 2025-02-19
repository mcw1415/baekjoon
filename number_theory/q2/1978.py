# N = int(input())
# numList = list(map(int, input().split()))

# count = N
# for num in numList:
#     if num == 1:
#         count -=1
#         continue
#     for i in range(2, int(num**0.5)+1): # 
#         if num % i == 0:
#             count -= 1
#             break
    
# print(count)

N = int(input())
numList = list(map(int, input().split()))

count = N
for num in numList:
    if num == 1:
        count -=1
        continue
    for i in range(2, num):  
        if num % i == 0:
            count -= 1
            break
        
    
print(count)

