def equalStacks(h1, h2, h3):
    s1 = [0]
    s2 = [0]
    s3 = [0]

    for i in h1[::-1]:
        s1.append(s1[-1] + i)
    for i in h2[::-1]:
        s2.append(s2[-1] + i)
    for i in h3[::-1]:
        s3.append(s3[-1] + i)

    while True:
        if s1[-1] >= s2[-1] and s1[-1] > s3[-1]:
            s1.pop(-1)
        if s2[-1] >= s3[-1] and s2[-1] > s1[-1]:
            s2.pop(-1)
        if s3[-1] > s2[-1] and s3[-1] >= s1[-1]:
            s3.pop(-1)

        if s1[-1] == s2[-1] and s2[-1] == s3[-1]:
            return s1[-1]
    
print(equalStacks([1,2,1,1], [1,1,2], [1,1]))
