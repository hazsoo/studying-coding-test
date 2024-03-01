def solution(s):
    answer = False
    stk = []
    for i in s:
        if i == '(':
            stk.append(1)
        else:
            try:
                stk.pop()
            except:
                return answer
    if not stk:
        answer = True
    return answer
    