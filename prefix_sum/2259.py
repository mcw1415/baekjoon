# A, B = map(int, input().split())
# arr = list(map(int, input().split()))

# prefix = [0 for _ in range(A+1)]

# for i in range(A):
#     prefix[i+1] = prefix[i] + arr[i]

# answer = []
# for i in range(B,A+1):
#     answer.append(prefix[i] - prefix[i-B])
    
# print(max(answer))
    
A, B = map(int, input().split())
arr = list(map(int, input().split()))

answer = []
for i in range(A+1):
    sum = 0
    if i+B-1 == len(arr)-1:
        for j in range(i, i+B):
            sum += arr[j]
        answer.append(sum)
        break
    else:
        for j in range(i, i+B):
            sum += arr[j]
        answer.append(sum)
        
print(max(answer))
    