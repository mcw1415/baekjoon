A, B = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

def recursion(A, B, arr, num_list, prefix_set):
    if B == 0:
        current = tuple(sorted(arr))
        if current not in prefix_set:
            prefix_set.add(current)
            print(*arr)
            return
    
    for i in num_list:
        if i in arr:
            continue
        arr.append(i)
        recursion(A, B-1, arr, num_list, prefix_set)
        arr.pop()
        
    
arr = []
prefix_set = set()
recursion(A, B, arr, num_list, prefix_set)