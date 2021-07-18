def isBalanced(s):
    mainStack = []
    dictMatch = {')': '(', '}': '{', ']':'['}
    for i in s:
        if i in '({[':
            mainStack.append(i)
        if i in ')}]':
            if len(mainStack) > 0:
                if dictMatch[i] ==  mainStack.pop(-1):
                    continue
                else:
                    return "NO"
            else:
                return "NO"
    if len(mainStack) == 0:
        return "YES"
    else:
        return "NO"



# ansss = []
# cases = []
# if __name__ == "__main__":
#     with open('./isBalancedTestCase.txt', 'r') as fp:
#         n = int(fp.readline())
#         for i in range(n):
#             cases.append(fp.readline())
#             ansss.append(isBalanced(cases[-1]))
#         fp.close()
#     with open('./isBalancedTestCaseAns.txt', 'r') as fp:
#         for i in range(n):
#             if ansss[i] == fp.readline().split("\n")[0]:
#                 print("TRUE")
#             else:
#                 print(cases[i])
#                 print("FALSE")


print(isBalanced('(])[{{{][)[)])(]){(}))[{(})][[{)(}){[(]})[[{}(])}({)(}[[()}{}}]{}{}}()}{({}](]{{[}}(([{]'))