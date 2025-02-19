N = int(input())

def recur(number):
    if number == 1:
        return
    
    if number % 2 == 0:
        print(2)
        recur(number // 2)
        return
    
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            print(i)
            recur(number // i)
            return
    
    print(number)

recur(N)
