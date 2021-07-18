def anagram(s):
    length = len(s)
    min = -1
    if length %2 == 0:
        s1 = s[:length//2]
        s2 = s[length//2 : ]
        print(s1, s2)
        ws1 = {}
        ws2 = {}
        for i in s1:
            if i in ws1:
                ws1[i] +=1
            else:
                ws1[i] = 1
        
        for i in s2:
            if i in ws2:
                ws2[i] +=1
            else:
                ws2[i] = 1
        
        for i in ws1.keys():
            print(ws1[i])
            # min += (ws2[i] - ws1[i])
        # print(min)

anagram("aaabbb")