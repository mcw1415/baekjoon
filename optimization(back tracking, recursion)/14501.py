N = int(input())
counsel_list = [list(map(int, input().split())) for _ in range(N)]

def recursion (idx, day, pay):
    global max_price
    if idx > N:
        return
    if idx == N:
        max_price = max(max_price, pay)
        return
    #예약한 경우
    recursion(idx + counsel_list[idx][0], day+ counsel_list[idx][0], pay + counsel_list[idx][1])
    #예약하지 않은 경우
    recursion(idx+1, day, pay)

max_price = -1
recursion(0, 0, 0)
print(max_price)