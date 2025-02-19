#1. 두 포인터가 가리키는 두 수의 합이 X를 만족한다면, s_p +1, e_p-1 => cnt +=1 
#2. 두 포인터가 가리키는 두 수의 합이 X를 초과한다면, e_p -= 1
#3. 두 포인터가 가리키는 두 수의 합이 X보다 작다면, s_p += 1
#4. 두 포인터가 만난다면 끝 

N = int(input())
arr = sorted(list(map(int, input().split())))
print(arr)
X = int(input())

s_p = 0
e_p = N-1

cnt = 0
while s_p != e_p:
    if arr[s_p] + arr[e_p] == X:
        s_p += 1
        e_p -= 1
        cnt += 1
        continue
    
    if arr[s_p] + arr[e_p] > X:
        e_p -= 1
        continue
    
    if arr[s_p] + arr[e_p] == X:
        s_p += 1
        continue

print(cnt)