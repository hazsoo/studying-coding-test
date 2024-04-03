br = input()
cnt = 0
st = []

for i in range(len(br)):
    if br[i] == "(":
        st.append("(")
    else:
        if br[i-1] == "(":
            st.pop()
            cnt += len(st)
        else:
            st.pop()
            cnt += 1
            
print(cnt)