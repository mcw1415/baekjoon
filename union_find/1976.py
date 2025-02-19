def _find(A):
    if A == parent[A]:
        return A
    else:
        parent[A] = _find(parent[A])
        return _find(parent[A]) 
    
def _union(A, B):
    A = _find(A)
    B = _find(B)
    
    if A == B:
        return
    
    if Rank[A] > Rank[B]:
        parent[B] = A
    elif Rank[A] < Rank[B]:
        parent[A] = B
    else:
        parent[B] = A
        Rank[A] += 1

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N+1)]
Rank = [0 for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            if parent[i+1] != parent[j+1]:
                _union(i+1, j+1)
            else:
                continue

plan = list(map(int, input().split()))
start_p = parent[plan[0]]
for p in plan:
    if start_p != parent[p]:
        print("NO")
        exit() #이건 신기하네
print("YES")

    
