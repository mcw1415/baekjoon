STR1 = list(input())
STR2 = list(input())
N1 = len(STR1)
N2 = len(STR2)

def recursion(idx1, idx2, count):
    global max_count 
    if idx1 == N1 or idx2 == N2:
        max_count = max(max_count, count)
        print(count)
        return 
    
    if STR1[idx1] == STR2[idx2]:
        count += 1
    
    #STR1에서 하나 빼기
    recursion(idx1 +1, idx2, count)
    
    #STR2에서 하나 빼기
    recursion(idx1, idx2 + 1, count)
    
max_count = 0
recursion(0, 0, 0)
print(max_count)