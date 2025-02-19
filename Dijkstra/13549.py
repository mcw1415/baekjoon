from collections import deque

A, B = map(int, input().split())
if A <= B:
    Start, End = A, B
    visited = [0 for _ in range(10001)]
    dist = [0 for _ in range(10001)]

    q = deque()
    q.append(Start)
    visited[Start] = 1

    while q:
        _x = q.popleft()
        if _x == End:
            break

        for mv_x, jump, sec in [[0, 2, 0], [-1, 1, 1], [1, 1, 1]]: #이 순서에 대한 내용도 있음
            dx = _x * jump + mv_x
            if 0 <= dx < 10001: #End를 넘기면 안됨 IndexError -> 범위 신경쓰자
                if visited[dx] == 0:
                    visited[dx] = 1
                    dist[dx] = dist[_x] + sec
                    q.append(dx)
        if dist[End] != 0:
            break
    
    print(dist[End])
                    
else:
    print(A-B)
                     
            
                
            
            