N = int(input())
arr = list(map(int, input().split()))
del_node = int(input())
tree = [[] for _ in range(N)]
start = 0

for i, p in enumerate(arr):
    if p == -1:
        start = i
    else:
        if p == del_node or i == del_node:
            continue
        else:
            tree[p].append(i)

        
def recursion(node):
    global count
    
    if len(tree[node]) == 0:
        count += 1
        return
    
    for next in tree[node]:
        recursion(next)
    
count = 0
if del_node == start:
    print(0)
else:
    recursion(start)
    print(count)
