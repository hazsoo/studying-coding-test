class Solution {
    boolean solution(String s) {
        boolean answer = true;

        int pCnt = 0;
        int yCnt = 0;
        
        String[] arr = s.split("");
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals("p") || arr[i].equals("P")) {
                pCnt += 1;
            } else if (arr[i].equals("y") || arr[i].equals("Y")) {
                yCnt += 1;
            }
        }
        
        if (pCnt != yCnt) {
            answer = false;
        }

        return answer;
    }
}