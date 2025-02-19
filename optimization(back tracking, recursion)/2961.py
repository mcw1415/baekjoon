N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

#재료를 사용하는 경우와 안하는 경우로 나누자
#-> 경우의 수를 나누는 것이 단순 반복으로는 어려울 것 같다.
#-> 재귀를 사용해보자

def recursion(idx, S, B, cnt):
    global gap
    
    if idx == N:
        if cnt > 0:
            gap = min(gap, abs(S-B))
            return 
        else:
            return
    
    #재료를 사용하는 경우
    recursion(idx+1, S * arr[idx][0], B + arr[idx][1], cnt + 1)
    
    #재료를 사용하지 않는 경우
    recursion(idx+1, S, B, cnt)
    
gap = 1e9
recursion(0,1,0,0)  

print(gap)