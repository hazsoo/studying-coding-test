t = int(input())
for _ in range(t):
    ps = input()
    vps = "YES"
    st = []

    for i in range(len(ps)):
        if ps[i] == "(":
            st.append(ps[i])
        else:
            try:
                st.pop()
            except:
                vps = "NO"
                break
        
    if st:
        vps = "NO"
    
    print(vps)