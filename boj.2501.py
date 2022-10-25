N, K = map(int, input().split())

result = 0

for i in range(1, N): #왜 N+1 까지일까? ## >> N과 K가 같을 경우에도 답이 나와야해서 + 1까지? >> 파이썬은 범위를 지정할때 앞에꺼부터 뒤에꺼 전까지.
    ## 이런게 궁금할때는 print 한번씩 다 찍어보기. 
    print("#", i)
    if N % i == 0:
        K -= 1
        if K == 0:
            result = i
            break

print(result)