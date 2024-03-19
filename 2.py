s = input()
pairs = {'(':')', '[':']', '{':'}'}
stack = []
for c in s:
    if c in pairs:
        stack.append(c)
    elif stack and pairs[stack.pop()] != c:
        print('False')
        break
else:
    print('True' if not stack else 'False')
