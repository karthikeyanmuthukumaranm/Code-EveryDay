def paranthesis_checker(exp):
    stack=[]
    paranthesis={'(':')','[':']','{':'}'}
    for ch in exp:
        if ch in paranthesis:
            stack.append(ch)
        elif ch in paranthesis.values():
            if not stack or paranthesis[stack[-1]] != ch:
                return False
            stack.pop()
    return not stack

exp=input('enter expression:')
print(paranthesis_checker(exp))