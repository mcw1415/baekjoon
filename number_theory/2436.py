A, B = map(int, input().split())

def GCD(A, B): #GCD => A = B*q + r => A -r = B*q
    
    while A % B != 0:
        temp = A % B
        A = B
        B = temp
    return B

def LCM(A,B):
    return (A*B)//GCD(A,B) #LCM(n1, n2) = (n1 * n2)//GCD(n1, n2) 

arr = []
#어떤 두 수 n1, n2의 GCD = 6, LCM = 180
for n1 in range(A, B, A):
    for n2 in range(A, B, A):
        if A * B == (n1 * n2):
            arr.append([n1, n2])           

sum = 1e9
ans_n1, ans_n2 = 0, 0
for n1, n2 in arr:
    if sum > (n1+n2):
        sum = n1+n2
        ans_n1, ans_n2 = n1, n2
        
print(ans_n1, ans_n2)
    
# arr = [] 
# gxl = gcd * lcm 
# for i in range(gcd, int(gxl**0.5)+ 1,gcd): #최소공약수부터 root(n1*n2)까지 
#     if GCD(i, (gxl//i)) == gcd: 
#         if LCM(i, (gxl//i)) == lcm:
#             arr.append((i, gxl//i))
            
# print(*arr[-1])
    
#다시 풀어보자...