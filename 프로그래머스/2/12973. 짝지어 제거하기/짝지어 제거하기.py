def solution(s):
    st = []
    for i in range(len(s)):
        if st and s[i] == st[-1]:
            st.pop()
        else:
            st.append(s[i])
    
    if len(st) == 0:
        return 1
    else:
        return 0