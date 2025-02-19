N = int(input()) 
numList = list(map(int, input().split())) 
numList.sort()  

def GCD(A, B):
    while A % B != 0:
        temp = A % B
        A = B
        B = temp
    return B

count = 0  
for i in range(N-1):  
    if GCD(numList[i], numList[i+1]) == 1:
        continue
    for j in range(numList[i] + 1, numList[i+1]):  
        if GCD(numList[i], j) == 1 and GCD(j, numList[i+1]) == 1:
            count += 1  
            break  
        if j == numList[i+1]-1:
            count += 2
print(count)
