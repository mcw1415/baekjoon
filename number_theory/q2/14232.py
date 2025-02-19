N = int(input())
count = 0
arr = []
def recur(number):
    global count, arr
    if number == 1:
        return
    
    if number % 2 == 0:
        count +=1
        arr.append(2)
        recur(number//2)
        return
    
    for i in range(3, int(number**0.5)+1, 2):
        if number % i == 0:
            count +=1
            arr.append(i)
            recur(number//i)
            return
    
    count +=1 
    arr.append(number)

recur(N)
print(count)
print(*arr)