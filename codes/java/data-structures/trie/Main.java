import java.util.*;

public class Main {
    // 최대 100개 단어 × 길이 20 + 루트
    static int[][] t = new int[2001][26];
    static int sz;
    static boolean[] fin = new boolean[2001];

    static void add(String s) {
        int u, x, i;

        u = 0;
        for (i = 0; i < s.length(); ++i) {
            x = s.charAt(i) - 'a';
            // 해당 문자로 이어지는 노드가 없으면 새 노드 생성
            if (t[u][x] == 0) t[u][x] = ++sz;
            u = t[u][x];
        }
        // 접두사 경로와 완성된 단어를 구분하는 끝 표시
        fin[u] = true;
    }

    static int find(String s) {
        int u, x, i;

        u = 0;
        for (i = 0; i < s.length(); ++i) {
            x = s.charAt(i) - 'a';
            // 해당 접두사 경로가 없으므로 검색 종료
            if (t[u][x] == 0) return -1;
            u = t[u][x];
        }
        return u;
    }

    public static void main(String[] args) {
        Scanner in;
        int n, q, i, u;
        String s, op;
        boolean ok;

        in = new Scanner(System.in);
        n = in.nextInt();
        q = in.nextInt();
        for (i = 0; i < n; ++i) {
            s = in.next();
            add(s);
        }

        for (i = 0; i < q; ++i) {
            op = in.next();
            s = in.next();
            u = find(s);

            // 단어 검색은 끝 표시까지 확인
            if (op.equals("word")) ok = u != -1 && fin[u];
            else ok = u != -1;

            if (ok) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}
