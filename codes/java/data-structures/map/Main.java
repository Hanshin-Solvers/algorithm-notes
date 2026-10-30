import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i;
        TreeMap<String, Integer> cnt;
        String s;

        in = new Scanner(System.in);
        n = in.nextInt();

        cnt = new TreeMap<>();
        for (i = 0; i < n; ++i) {
            s = in.next();

            // 처음 등장한 단어는 0부터 횟수 증가
            cnt.put(s, cnt.getOrDefault(s, 0) + 1);
        }

        // 정렬 맵의 키 순서대로 단어와 횟수 출력
        for (Map.Entry<String, Integer> e : cnt.entrySet()) {
            System.out.println(e.getKey() + " " + e.getValue());
        }
    }
}
