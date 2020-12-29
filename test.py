for a in range(2,11): # a는 2~10 까지 반복
    for q in range(2,a): # q는 2에서 a-1 까지 반복
        if a%q ==0: #a가 q로 나누어 떨어지면
            print(a,"는 소수아님") #소수가 아님을 출력하고
            break #루프에서 빠져나감
    else: #위에 있는 for문(q)을 끝까지 수행했으면
        print(a,"는 소수임") #소수라고 출력함
