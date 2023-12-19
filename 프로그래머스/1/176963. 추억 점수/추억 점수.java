import java.util.HashMap;
import java.util.Map;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        Map<String, Integer> nameYearing = new HashMap<>();
        for (int i = 0; i < name.length; i++) {
            nameYearing.put(name[i], yearning[i]);
        }
        for (int i = 0; i < photo.length; i++) {
            int year = 0;
            for (int j = 0; j < photo[i].length; j++) {
                if (nameYearing.containsKey(photo[i][j]))
                    year += nameYearing.get(photo[i][j]);
            }
            answer[i] = year;
        }
        return answer;
    }
}