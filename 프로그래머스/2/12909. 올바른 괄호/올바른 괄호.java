import java.util.Stack;

class Solution {
    boolean solution(String s) {
        Stack<Character> st = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                st.push(s.charAt(i));
            }
            else {
                if (!st.empty() && st.peek() == '(') {
                    st.pop();
                }
                else {
                    return false;
                }
            }
        }

        return st.empty() ? true : false;
    }
}