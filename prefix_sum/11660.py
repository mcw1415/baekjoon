import sys
input = sys.stdin.readline

A, B = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(A)]
xy_list = [list(map(int, input().split())) for _ in range(B)]

for point in xy_list:
    x1, y1, x2, y2 = point
    sum = 0
    for x in range(x1-1, x2):
        for y in range(y1-1, y2):
            sum += graph[x][y]        
    print(sum)    
#답은 나오나 시간 초과 문제 -> 시간초과 문제

# A, B = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(A)]

# xy_list = [list(map(int, input().split())) for _ in range(B)]

# prefix = [[0 for _ in range(A+1)] for _ in range(A+1)]

# for x in range(1, A+1):
#     for y in range(1, A+1):
#         prefix[x][y] = prefix[x][y-1] + prefix[x-1][y] - prefix[x-1][y-1] + graph[x-1][y-1]

# for point in xy_list:
#     x1, y1, x2, y2 = point
#     answer = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
#     print(answer)
        