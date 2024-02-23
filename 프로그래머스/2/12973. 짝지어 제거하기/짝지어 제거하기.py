def solution(s):
    st = []
    for i in s:
        if st and st[-1] == i:
            st.pop()
            continue
        st.append(i)
    return int(not st)