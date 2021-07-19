def waiter(number, q):
    firstQPrimes = []
    ct = 1
    flag = 0
    i = 2

    while ct <= q:
        flag = 0
        for j in range(2, i//2+1):
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            firstQPrimes.append(i)
            ct+=1
        i+=1
    
    a = number[::-1]
    b = []
    answer = []

    for i in range(q):
        temp = []
        for j in a:
            if j%firstQPrimes[i] == 0:
                b.append(j)
            else:
                temp.append(j)
        answer.extend(b[::-1])
        b = []
        a = temp[::-1]

    answer.extend(a)
    return answer
    

print(waiter([3,3,4,4,9], 2))