A, B = map(int, input().split())

# for i in range(1, A+1):
#     for j in range(1, A+1):
#         print(i, j)
        
#i, j가 B가 2로 2개일 경우 출력인데, for문으로 계속하기엔 너무 컴퓨터에게 의존하는 경향이 강함. 어떻게 B를 활용하여 for문을 유동적으로 짤 수 있을까에 답이 잘 안보임
#따라서 재귀를 사용해보겠다

def recursion(A, B, arr):
    if B == 0:
        print(*arr)
        return
    
    for i in range(1, A+1):
        if i in arr:
            continue
        arr.append(i)
        recursion(A, B-1, arr)
        arr.pop()

arr =[]
recursion(A, B, arr)

#문제 조건 잘 읽자
