from collections import deque

N = int(input())
map = [list(map(str, input().rstrip())) for _ in range(N)]
answer = [0, 0]

for whether in range(2):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    count = 1
    
    for s_y in range(N):
        for s_x in range(N):
            if visited[s_y][s_x] != 0:
                continue
            
            s = map[s_y][s_x]
            
            q = deque()
            q.append([s_y,s_x])
            visited[s_y][s_x] = count

            while q:
                y, x = q.popleft()

                for mv_y, mv_x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dy, dx = mv_y + y, mv_x + x
                    if whether == 0: #정상
                        if 0 <= dy < N and 0 <= dx < N:
                            if visited[dy][dx] == 0 and s == map[dy][dx]:
                                visited[dy][dx] = count
                                q.append([dy, dx])
                    else: #적록색약
                        if 0 <= dy < N and 0 <= dx < N:
                            if visited[dy][dx] == 0:
                                if s == map[dy][dx]: #출발점 색과 같으면
                                    visited[dy][dx] = count
                                    q.append([dy, dx])
                                elif (s == 'R' and map[dy][dx] == 'G') or (s == 'G' and map[dy][dx] == 'R'): #출발점 색과 다르지만 빨강과 초록 관계일 경우
                                    visited[dy][dx] = count
                                    q.append([dy, dx])
            
            count += 1
    answer[whether] = count - 1
    #print(max(map(max, visited)))

print(*answer)
    
    

    

    

    
