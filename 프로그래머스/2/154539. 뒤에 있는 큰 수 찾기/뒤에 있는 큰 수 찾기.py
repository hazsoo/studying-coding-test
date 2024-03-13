def solution(numbers):
    answer = [-1]*len(numbers)
    st = []
    for i in range(len(numbers)-1,-1,-1):
        while st and numbers[i] >= st[-1]:
            st.pop()

        if st:
            answer[i] = st[-1]

        st.append(numbers[i])

    return answer