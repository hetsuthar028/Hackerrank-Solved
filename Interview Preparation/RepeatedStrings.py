# def repeatedString(s, n):
#     ct = 0
#     l = len(s)
#     rs = 0
#     for i in s:
#         if i == 'a':
#             ct +=1
#     rs = n*ct // l
#     for i in range(n % l):
#         if s[i] == 'a':
#             rs +=1
#     return rs

def repeatedString(s, n):
    ct = 0
    l = len(s)
    for i in s:
        if i == 'a':
            ct+= 1

    ct*= int(n / l)
    for i in range(0, n % l):
        if s[i] == 'a':
            ct+= 1
    return ct

print(repeatedString('aba', 10))