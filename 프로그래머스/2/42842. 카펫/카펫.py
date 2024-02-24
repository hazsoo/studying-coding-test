def solution(brown, yellow):
    answer = []
    area = brown + yellow
    d = []
    for i in range(area, 0, -1):
        if area % i == 0:
            d.append(i)
    st = []
    for i in range(len(d)):
        if st and (st[0]-2) * (st[1]-2) == yellow:
            answer.append(st[0])
            answer.append(st[1])
            st.pop()
            st.pop()
            break
        elif st:
            st.pop()
            st.pop()
        st.append(d[i])
        st.append(d[-i-1])
    return answer