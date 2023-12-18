import java.util.HashMap;
import java.util.Map;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};
        Map<String, Integer> playerMap = new HashMap<>();
        for (int i = 0; i < players.length; i++) {
            playerMap.put(players[i], i);
        }
        
        for (String c : callings) {
            int rank = playerMap.get(c);
            String temp = players[rank - 1];
            players[rank - 1] = c;
            players[rank] = temp;

            playerMap.put(c, rank-1);
            playerMap.put(temp, rank);
        }

        answer = players;
        return answer;
    }
}