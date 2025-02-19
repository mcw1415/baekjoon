N = int(input())
graph = [[] for _ in range(128)]
pre_o = []
in_o = []
post_o = []

for _ in range(N):
    a, b, c = map(str, input().split())
    a = ord(a)
    b = ord(b)
    c = ord(c)
    graph[a].append(b)
    graph[a].append(c)

def recursion(node):
    if node == ord('.'):
        return
    
    pre_o.append(chr(node))
    #왼쪽
    recursion(graph[node][0])
    in_o.append(chr(node))
    #오른쪽
    recursion(graph[node][1])
    post_o.append(chr(node))
    

recursion(ord('A'))

for pr in pre_o:
    print(pr, end="")

print()
for i in in_o:
    print(i, end="")
print()
for po in post_o:
    print(po, end="")