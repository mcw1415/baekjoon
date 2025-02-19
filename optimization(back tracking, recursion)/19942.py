N = int(input())
a_, b_, c_, d_ = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def recursion(idx, A, B, C, D, cost, use_idx):
    global price, result_idx
    if idx == N:
        if A >= a_ and B >= b_ and C >= c_ and D >= d_:
            if price > cost:
                price = cost
                result_idx = use_idx[:]
            elif price == cost:
                i = 0
                cp = min(len(result_idx), len(use_idx))
                while cp > i:
                    if result_idx[i] > use_idx[i]:
                        result_idx = use_idx[:]
                        break
                    elif result_idx[i] < use_idx[i]:
                        break
                    else:
                        i+= 1
                if len(result_idx) > len(use_idx):  
                    result_idx = use_idx[:]
                
                # if result_idx > use_idx:
                #     result_idx = use_idx[:]    
        return 
    
    use_idx.append(idx+1)
    recursion(idx + 1, A + arr[idx][0], B + arr[idx][1], C + arr[idx][2], D + arr[idx][3], cost + arr[idx][4], use_idx)
    use_idx.pop()
    
    recursion(idx + 1, A, B, C, D, cost, use_idx)
	
price = 1e9
result_idx = []
use_idx = []
recursion(0, 0, 0, 0, 0, 0, use_idx)

if result_idx:
    print(price)
    print(*result_idx)
else:
    print(-1)