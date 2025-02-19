n = int(input())

for _ in range(n):
    key = int(input())
    
    for i in range(2, 1000001): #2~1_000_000까지의 완전탐색
        if key % i == 0: #백만 이하의 약수가 존재하면 NO 출력 후 break
            print("NO")
            break
        
        if i == 1000000: #백만 이하의 약수가 존재하지 않으면 YES 출력
            print("YES")
#문제 내용 중에서 만일 S의 모든 소인수가 백만보다 크다면 적절한 암호키이다.
#-> key의 약수 중 1을 제외하고 백만보다 크다면 답으로 인정해라 


            
