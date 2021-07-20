def twoStrings(s1, s2):
    s1W = {}
    s2W = {}
    for i in s1:
        s1W[i] = 1
    for i in s2:
        if i in s1W:
            return "YES"
    return "NO"

print(twoStrings("hi", "world"))