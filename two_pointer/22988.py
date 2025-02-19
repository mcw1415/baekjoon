N, X = map(int, input().split())
arr = sorted(list(map(int, input().split())))

s_p = 0
e_p = N-1

count = 0
sub_count = 0

while s_p <= e_p:
    
    if arr[e_p] == X:
        count += 1
        e_p -= 1
        continue
    
    if s_p == e_p:
        sub_count += 1
        break

    total = arr[s_p] + arr[e_p]
    
    #합친 용량이 총 용량의 절반보다 크거나 같다면, 무조건 하나는 생김
    if total >= X/2:
        s_p += 1
        e_p -= 1
        count += 1
        
    #합친 용량이 총 용량의 절반보다 작다면, 다른 카운트를 세자
    if total < X/2:
        s_p += 1
        sub_count += 1
        
count += sub_count//3
print(count)
# 7 13
# 0 1 2 3 5 8 13

# 6 1
# 0 0 0 0 0 0
# 0.5 0.5 0.5
# 세 개의 빈병으로 한 병을 채울 수 있다.

#6 6 6일 경우에는 맞아
#근데 합친 용량이 1 1 1 아러면 