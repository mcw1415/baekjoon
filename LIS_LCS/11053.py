N = int(input())
arr = list(map(int, input().split()))
m_len = 1

for i in range(1, N):
    _len = 1
    _mv = 0 
    for j in range(i):  
        if arr[i] > arr[j] and _mv < arr[j]:
            _mv = arr[j]
            _len += 1
                
    m_len = max(m_len, _len)

print(m_len)

    

# 6
# 10 20 10 30 20 50
# 10 20 60 30 20 50
