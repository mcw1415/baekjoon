A, B = map(int, input().split())

def recursion(A, B, arr):
    if B == 0:
        print(*arr)
        return
    
    for i in range(1, A+1):
        arr.append(i)
        recursion(A, B-1, arr)
        arr.pop()
    
arr = []
recursion(A, B, arr)