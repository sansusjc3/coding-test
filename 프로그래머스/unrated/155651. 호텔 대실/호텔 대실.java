import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        Map<Integer, Integer> cnt = new HashMap<>();

        for (String[] time : book_time) {
            String[] a = time[0].split(":");
            int start = Integer.parseInt(a[0]) * 60 + Integer.parseInt(a[1]);

            String[] b = time[1].split(":");
            int end = Integer.parseInt(b[0]) * 60 + Integer.parseInt(b[1]) + 10;

            for (int i = start; i < end; i++) {
                if (!cnt.containsKey(i)) {
                    cnt.put(i, 1);
                } else {
                    cnt.put(i, cnt.get(i) + 1);
                }
            }
        }

        answer = Collections.max(cnt.values());

        return answer;
    }
}