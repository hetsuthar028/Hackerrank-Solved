def checkMagazine(magazine, note):
    magwords = {}
    for i in magazine:
        if i not in magwords:
            magwords[i] = 1
        else:
            magwords[i] += 1
    
    for word in note:
        if word in magwords and magwords[word] > 0:
            magwords[word] -=1
        else:
            print("No")
            return
    print("Yes")