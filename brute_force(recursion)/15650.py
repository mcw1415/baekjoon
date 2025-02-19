# A, B = map(int, input().split())

# def recursive(A, B, arr, prefix):
#     if B == 0 :
#         prefix.append(arr)
#         print(*arr)
#         return
    
#     for i in range(1, A+1):
#         if i in arr:
#             continue
#         arr.append(i)
#         recursive(A, B-1, arr, prefix)
#         arr.pop()
        

# prefix = []
# arr = []
# recursive(A, B, arr, prefix)

A, B = map(int, input().split())

def recursive(A, B, arr, prefix_set):
    if B == 0:
        # 현재 수열을 튜플로 변환해 정렬 후 중복 여부 확인
        current = tuple(sorted(arr))
        if current not in prefix_set:
            prefix_set.add(current)  # 집합에 추가
            print(*arr)
        return
#sort와 sorted의 차이점은 sorted는 원래 리스트를 변경하지 않는다는 것 

    for i in range(1, A + 1):
        if i in arr:
            continue
        arr.append(i)
        recursive(A, B - 1, arr, prefix_set)
        arr.pop()

prefix_set = set()  
arr = []
recursive(A, B, arr, prefix_set)
print(prefix_set)
