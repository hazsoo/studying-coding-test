def solution(s):
    cnt = 0
    s_pairs = {
        ']':'[',
        '}':'{',
        ')':'('
    }
    
    for i in range(len(s)):
        st = []
        rot = s[i:] + s[:i]
        
        for j in rot:
            if j in ')}]':
                if st and st[-1] == s_pairs[j]:
                    st.pop(-1)
                    continue
                else:
                    break
            st.append(j)
        
        else:
            if not st:
                cnt += 1
                
    return cnt