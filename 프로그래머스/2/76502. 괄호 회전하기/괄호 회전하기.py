def solution(s):
    cnt = 0
    s_pairs = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    
    for i in range(len(s)):
        st = []
        rot = s[i:] + s[:i]
        
        for r in rot:
            if r in ')}]':
                if st and st[-1] == s_pairs[r]:
                    st.pop(-1)
                    continue
                else:
                    break
            st.append(r)
        
        else:
            if not st:
                cnt += 1
            
    return cnt
            