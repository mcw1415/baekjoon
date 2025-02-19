import sys
sys.setrecursionlimit(40000)

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]
child = [0 for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split()) 
    graph[a].append(b)
    graph[b].append(a)

def recursion(node, prev):
    
    parent[node] = prev
    
    for next in graph[node]:
        if next != prev:
            parent[next] = node
            recursion(next, node)
    child[prev] += 1
    
recursion(1, 0)

for i in range(2, N+1):
    print(parent[i])


