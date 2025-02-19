import sys
sys.setrecursionlimit(40000)

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
number = 1
answer = []

def recursion(_y, _x):
    global number, count
    
    for mv_y, mv_x in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        dy = _y + mv_y
        dx = _x + mv_x
        
        if 0 <= dy < N and 0 <= dx < N:
            if visited[dy][dx] == 0 and graph[dy][dx] == 1:
                visited[dy][dx] = number
                count += 1
                recursion(dy, dx)
    
                
for y in range(N):
    for x in range(N):
        if graph[y][x] != 1 or visited[y][x] != 0:
            continue 
        count = 1
        visited[y][x] = number
        recursion(y, x)
        answer.append(count)
        number += 1

print(len(answer))
for i in sorted(answer):
    print(i)
            