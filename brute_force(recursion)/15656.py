A, B = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

def recursion(A, B, arr, num_list):
    if B == 0:
        print(*arr)
        return
    
    for i in num_list:
        arr.append(i)
        recursion(A, B-1, arr, num_list)
        arr.pop()
        
    
arr = []
recursion(A, B, arr, num_list)