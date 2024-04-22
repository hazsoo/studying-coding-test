t = int(input())

for _ in range(t):
    ps = input()
    st = []
    vps = "YES"

    for i in range(len(ps)):
        if ps[i] == "(":
            st.append("(")
        else:
            try:
                st.pop()
            except:
                vps = "NO"
                break

    if st:
        vps = "NO"

    print(vps)