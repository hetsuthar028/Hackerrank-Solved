def matchingStrings(strings, queries):
    s = {}
    ans = []
    for i in strings:
        if i in s:
            s[i] +=1
        else:
            s[i] = 1

    for i in queries:
        try:
            ans.append(s[i])
        except:
            ans.append(0)

    for i in ans:
        print(i)

matchingStrings(['abcde', 'sdakljf', 'asdjf', 'na', 'basdn', 'sdakljf', 'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdakljf', 'asdjf'], ['abcde', 'sdakljf', 'asdjf', 'na', 'basdn'])