def _union(A, B):
    a = _find(A)
    b = _find(B)
    
    if a == b:
        return
    if Rank[a] > Rank[b]:
        parent[b]= a
    elif Rank[a] < Rank[b]:
        parent[a]= b
    else:
        parent[b]= a
        Rank[a] += 1
    
def _find(A):
    if A == parent[A]:
        return A
    else:
        #A의 부모를 부모의 부모로 바꾸기
        parent[A] = _find(parent[A])
        return parent[A]
        
N, M = map(int, input().split())
parent = [i for i in range(N+1)]
Rank = [0 for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    if _find(A) != _find(B):
        _union(A, B)

plan = list(map(int, input().split()))

answer = 0
for i in range(1, len(plan)):
    if _find(plan[i-1]) != _find(plan[i]):
        answer += 1

print(answer)