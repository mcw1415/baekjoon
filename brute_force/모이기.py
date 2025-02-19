n = int(input())
list = [list(map(int, input().split())) for _ in range(n)]
fi_answer = [int(1e9)] * n #초기 배열 생성
x_list = []
y_list = []
for x, y in list: #후보군 리스트 생성
    x_list.append(x)
    y_list.append(y)

for x_pnt in x_list:
    for y_pnt in y_list: 
        answer = []
        for x, y in list: #입력 x, y #어느 한 점에서 입력위치로부터의 거리 최솟값 계산
            answer.append(abs(x_pnt-x) + abs(y_pnt-y)) # ex) [1,4,6,7], [0,2,3,4]
        
        answer.sort()
        distance_cost = 0 #k번째 마다 이동 비용의 최소값 계산            
        for i in range(n):
            distance_cost += answer[i] #1~k
            if fi_answer[i] > distance_cost:
                fi_answer[i] = distance_cost
print(*fi_answer)
            

            
                
        
        
            
                
            
        