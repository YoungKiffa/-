s = input()
pairs = {'(':')', '[':']', '{':'}'}
stack = []
for c in s:
    if c in pairs:
        stack.append(c)
    elif stack and pairs[stack[-1]] == c:
        stack.pop()
    else:
        print('False')
        break
else:
    print('True' if not stack else 'False')
