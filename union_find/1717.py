N, M = map(int, input().split())
parent = [i for i in range(N+1)]
Rank = [0 for _ in range(N+1)]
answer = []

def _union(A, B): #두 수를 합
    a = _find(A)
    b = _find(B)
    if a == b:
        return
    if Rank[a] > Rank[b]:
        parent[b] = a
    elif Rank[a] < Rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        Rank[a] += 1
        

def _find(A): #조상 확인
    if A == parent[A]:
        return A
    else:
        parent[A] = _find(parent[A]) #경로 단축: 부모를 조상으로 통일 시켜버리는 것
        return _find(parent[A])

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        if _find(b) == _find(c):
            answer.append("YES")
        else:
            answer.append("NO")  
    else:
        _union(b,c)

print(parent)
for ans in answer:
    print(ans)
    
